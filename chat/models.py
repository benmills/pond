from mongoengine import *
from mongoengine.django.auth import User
from datetime import datetime, date, timedelta
from time import mktime
import time

class Chat(Document):
	message = StringField()
	user = ReferenceField(User)
	time = FloatField()
	
	def save(self):
		self.time = time.time()
		
		#Update poster inorder to get who is online
		self.user.last_login = datetime.now()
		self.user.save()
		super(Chat, self).save()
		
	def outdated(self):
		return (time.time() - self.time) > 10000
		
	def timedelta(self):
		return int(time.time() - self.time)/60