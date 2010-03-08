from mongoengine import *

class CommandInput(Document):
	command = StringField()
	output = StringField()
	
class Chat(Document):
	username = StringField()
	message = StringField()