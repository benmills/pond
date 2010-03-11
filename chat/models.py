from mongoengine import *
from datetime import datetime, date, timedelta
from time import mktime
import time

class CommandInput(Document):
	command = StringField()
	output = StringField()
	
	def save(self):
		if len(CommandInput.objects(command=self.command)) is 0:
			super(CommandInput, self).save()
		else:
			return 'Command already exists'

class Chat(Document):
	username = StringField()
	message = StringField()
	time = FloatField()
	
	def save(self):
		self.time = time.time()
		super(Chat, self).save()
		
	def outdated(self):
		return (time.time() - self.time) > 10000
		
	def timedelta(self):
		return int(time.time() - self.time)/60
			
	def output(self):
		c = filter(lambda c: c.command == self.message, CommandInput.objects)
		if c: return c[0].output
		else: return self.message