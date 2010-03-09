from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from chat.models import *

def index(request):
	message = ''
	if request.method == 'POST' and request.POST['command_name'] and request.POST['command_output']:
		c = CommandInput(command=request.POST['command_name'], output=request.POST['command_output'])
		if len(CommandInput.objects(command=c.command)) == 0:
			c.save();
		else:
			message = 'Command already exists'
		
	return render_to_response('index.html', {
		'commands': CommandInput,
		'message': message,
		'chat': Chat.objects.order_by('_id'),
	})
	
def post_chat(request):
	m = None
	if request.method == 'POST' and request.POST['message']:
		msg = request.POST['message']
		for c in CommandInput.objects:
			if msg == c.command:
				msg = c.output
				break
		
		user = 'anon'
		if request.POST['username']:
			user = request.POST['username']
			
		m = Chat(username=user, message=msg)
		m.save()
	return render_to_response('post.html', {
		'm': m
	})
		
def check_chat(request):
	m = Chat.objects.order_by('_id')
	m = m[len(m)-1]
	return render_to_response('post.html', {
		'm': m
	})
	
def get_chat(request):
 	return render_to_response('chat_feed.html', {
		'chat': Chat.objects.order_by('_id')
	})