// Page load
var orig = $('div.console').html();
var title = $('title').html();
var blink_title = '';
var submitting = false;
var updating = false;

$(window).focus(function() {
	$('title').html(title);
	blink_title = '';
});
$('input#input').focus();

function update_title() {;
	if (blink_title.length > 0) {
		if ($('title').html() != '-') $('title').html('-');
		else $('title').html(blink_title);
	} 
}

$('div.console').attr({scrollTop: $("div.console").attr("scrollHeight")});
if ($.cookie('username')) $('input#username').val($.cookie('username'));

// Update
function check_chat() {
	if (updating == false) {
		$.get('/check', function(data) {
			if ($('div.console p:last span.time').html() < parseFloat(data)) {
				updating = true;
				$.get('/feed/'+$('div.console p:last span.time').html(), function(data) {
					console.log('UPDATE');
					blink_title = 'talking'
					$("div.console").append(data).attr({scrollTop: $("div.console").attr("scrollHeight")});
					updating = false;
				});
			}
		});
	}
	update_title();
}
setInterval ("check_chat()", 500);

// Submit line
$('form#command').submit(function(e) {
	if (updating) return false;
	if ($('input#input').val() == '/help') {
		$("div.console").append($('.help').html()).attr({scrollTop: $("div.console").attr("scrollHeight")});
		$('input#input').val('').focus();
		return false;
	}
	
	$.cookie('username', $('input#username').val());
	$('form#command input').attr('disabled', 'disabled');
	updating = true;
	$.ajax({
		type: 'POST',
		data: {message: $('input#input').val(), username: $('input#username').val()},
		url: '/post/',
		success: function(data) {
			$('div.console').append(data).attr({scrollTop: $("div.console").attr("scrollHeight")});
			$('input#input').val('').focus();
			$('form#command input').attr('disabled', '');
			updating = false;
		}
	});
	return false;
});

