var orig = $('div.console').html();

// Post Chat
$('form#command').submit(function(e) {
	e.preventDefault();
	$.ajax({
		type: 'POST',
		data: {message: $('input#input').val(), username: $('input#username').val()},
		url: '/post/',
		success: function(data) {
			$('div.console').append(data);
			$('input#input').val('').focus();
		}
	});
	return false;
});

// use a command
$('a.command').live('click', function(e) {
	e.preventDefault();
});

// Update Chat
function check_chat() {
	$.ajax({
		type: 'GET',
		url: '/check/',
		success: function(data) {
			if ($('div.console p:last').html() != $(data).html()) {
				$.ajax({
					url: '/feed/',
					success: function(data) {
						$("div.console").html(data).attr({scrollTop: $("div.console").attr("scrollHeight")});;
					}
				});
			}
		}
	})
}

setInterval ("check_chat()", 1000);