// Page load
var orig = $('div.console').html();
$('div.console').attr({scrollTop: $("div.console").attr("scrollHeight")});
if ($.cookie('username')) $('input#username').val($.cookie('username'));

// Submit line
$('form#command').submit(function(e) {
	$.cookie('username', $('input#username').val());
	$.ajax({
		type: 'POST',
		data: {message: $('input#input').val(), username: $('input#username').val()},
		url: '/post/',
		success: function(data) {
			$('div.console').append(data).attr({scrollTop: $("div.console").attr("scrollHeight")});
			$('input#input').val('').focus();
		}
	});
	return false;
});

// Commands
$('a.command').live('click', function(e) {
	e.preventDefault();
	$('input#input').val($('input#input').val()+$(this).html());
});

// Update
function check_chat() {
	$.get('/check/', function(data) {
			if ($('div.console p:last').html() != $(data).html()) {
				$.get('/feed/', function(data) {
						$("div.console").html(data).attr({scrollTop: $("div.console").attr("scrollHeight")});
				});
			}
	});
}

setInterval ("check_chat()", 1000);