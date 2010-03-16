from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime, timedelta
from chat.models import *
from mongoengine.django.auth import User

def index(request):
	message = None
	
	#Login
	if request.method == 'POST' and request.POST['name'] and request.POST['password']:
		username = str(request.POST['name']).lower()
		
		u = authenticate(username=username, password=request.POST['password'])
		if u is None:
			if request.POST.has_key('should_register'):
				if len(User.objects(username=request.POST['name'])) == 0:
					u = User(username=username)
					u.set_password(request.POST['password'])
					u.save()
					auth_login(request, authenticate(username=username, password=request.POST['password']))
				else:
					message = 'Sorry, that username is taken :('
			else:
				message = 'Sorry, the name or password was wrong. Do you not have an account yet? Just fill out the form and check "New Account"'
		else:
			auth_login(request, u)
		
	#online users
	delta = datetime.now() - timedelta(minutes=20)
	online = User.objects(last_login__gt=delta)
	
	return render_to_response('chat/chat.html', {
		'message': message,
		'chat': Chat.objects.order_by('+time'),
		'user': request.user,
		'online': online
	})
	
def post_chat(request):
	m = None
	if request.method == 'POST' and request.POST['message']:
		m = Chat(user=request.user, message=request.POST['message'])
		m.save()
		
	return render_to_response('chat/post.html', {
		'm': m
	})
		
def check_chat(request):
	return render_to_response('chat/check.html', {
		'm': Chat.objects.order_by('-time').first()
	})
	
def get_chat(request, date=0):
 	return render_to_response('chat/chat_feed.html', {
		'chat': Chat.objects.filter(time__gt=(float(date)+.01)).order_by('+time')
	})
	
def register(request):
	if request.method == 'POST' and request.POST['name'] and request.POST['password']:
		u = User(username=request.POST['name'])
		u.set_password(request.POST['password'])
		u.save()
	return render_to_response('user/register.html')