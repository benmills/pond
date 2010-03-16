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
if ($("div#chat").html()) setInterval ("check_chat()", 900);

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

