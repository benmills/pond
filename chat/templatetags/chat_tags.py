from django import template
from django.core.urlresolvers import reverse
import logging

register = template.Library()	

@register.filter
def imageize(obj):
	is_image = -1
	types = ('jpg', 'jpeg', 'gif', 'png')
	
	for t in types:
		if obj.find(t) > -1:
			is_image = 2
			break
			
	if is_image > -1:
		return "<img src='"+obj+"'>"
	else:
		return obj