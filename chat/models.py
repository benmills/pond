from mongoengine import *
from datetime import datetime, date, timedelta

class CommandInput(Document):
	command = StringField()
	output = StringField()
	
class Chat(Document):
	username = StringField()
	message = StringField()
	time = DateTimeField(default=datetime.now)