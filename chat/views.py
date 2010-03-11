from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from chat.models import *

def index(request):
	if request.method == 'POST' and request.POST['command_name'] and request.POST['command_output']:
		message = CommandInput(command=request.POST['command_name'], output=request.POST['command_output']).save()
	else: message = None
		
	return render_to_response('index.html', {
		'commands': CommandInput,
		'message': message,
		'chat': Chat.objects.order_by('+time')[100:],
	})
	
def post_chat(request):
	m = None
	if request.method == 'POST' and request.POST['message']:
		m = Chat(username=request.POST['username'], message=request.POST['message'])
		m.save()
		
	return render_to_response('post.html', {
		'm': m
	})
		
def check_chat(request):
	return render_to_response('check.html', {
		'm': Chat.objects.order_by('-time').first()
	})
	
def get_chat(request, date=0):
 	return render_to_response('chat_feed.html', {
		'chat': Chat.objects.filter(time__gt=(float(date)+.01)).order_by('+time')
	})