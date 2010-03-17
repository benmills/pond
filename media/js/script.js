// Page load
var orig = $('div.console').html();
var title = $('title').html();
var blink_title = '';
var focused = true;
var submitting = false;
var updating = false;

$(window).focus(function() {
	$('title').html(title);
	blink_title = '';
	focused = true;
}).blur(function() {
	focused = false;
});

$('input#input').focus();

function update_title() {;
	if (blink_title.length > 0 && focused == false) {
		if ($('title').html() != '-') $('title').html('-');
		else $('title').html(blink_title);
	} 
}

function get_active_users() {
	$.ajax({
		url: '/active_users/',
		success: function(data) {
			$("#online_users").html($(data).html());
		}
	});
}

function update_time() {
	$("div.chat_line span.timestamp").each(function() {
		var timestamp = parseFloat($(this).html());
		var ts = Math.round(new Date().getTime() / 1000);
		var delta = ts - timestamp;
		var output = "";
		var time = 0;
		
		//console.log(delta);
		
		if (delta < 60) {
			output = "seconds";
			time = delta;
		} else {
			// Minutes
			time = delta/60;
			if ((time/60)>1) {
				time = time/60;
				if ((time/24)>1) {
					time = time/24;
					output = 'days';
				} else output = "hours";
			} else output = "minutes";
		}
		
		time = Math.round(time);
		if (time == 1) output = output.substr(0, output.length-1);
		
		$(this).siblings('p.time').html(Math.round(time)+" "+output+" ago");
	});
}
update_time();

$('div#chat').attr({scrollTop: $("div#chat").attr("scrollHeight")});

// Update
$(document).ajaxError(function() {
	window.location = window.location;
});
function check_chat() {
	if (updating == false) {
		$.ajax({
			url: '/check',
			success: function(data) {
				if ($('div#chat div:last span.timestamp').html() < parseFloat(data)) {
					updating = true;
					$.ajax({
						url: '/feed/'+$('div#chat div:last span.timestamp').html(),
						success: function(data) {
							if (focused == false) blink_title = 'Ripple'
							$("div#chat").append(data).attr({scrollTop: $("div#chat").attr("scrollHeight")});
							updating = false;
						},
						error: function() {
							window.location = window.location;
						}
					});
				}
			},
			error: function() {
				window.location = window.location;
			}
		});
	}
	update_title();
}
if ($("div#chat").html()) {
	setInterval("update_time()", 60000)
	setInterval("check_chat()", 900);
	setInterval("get_active_users()", 60000);
}

// Submit line
$('form#add_post').submit(function(e) {
	if (updating) return false;
	if ($('input#input').val() == '/help') {
		$("div#chat").append($('.help').html()).attr({scrollTop: $("div#chat").attr("scrollHeight")});
		$('input#input').val('').focus();
		return false;
	}
	
	$('form#command input').attr('disabled', 'disabled');
	updating = true;
	$.ajax({
		type: 'POST',
		data: {message: $('input#input').val(), username: $('input#username').val()},
		url: '/post/',
		success: function(data) {
			$('div#chat').attr({scrollTop: $("div#chat").attr("scrollHeight")});
			$('input#input').val('').focus();
			$('form#command input').attr('disabled', '');
			updating = false;
		}
	});
	return false;
});

