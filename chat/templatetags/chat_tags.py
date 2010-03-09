from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import urlize
import logging
import re

register = template.Library()	

@register.filter
def imageize(obj):
	types = ('.jpg', '.jpeg', '.gif', '.png')
	line = obj.split(' ')
	output = ''
	
	for l in line:
		# Images
		is_image = -1
		for t in types:
			if l.find(t) > -1:
				is_image = 2
				break
		if is_image > 0:
			l = "<img src='"+l+"'>"
		
		# Youtube
		elif l.find('youtube.com') > 0:
			regex = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
			match = regex.match(l)
			if match:
				video_id = match.group('id')
				l = """
						<object width="425" height="344">
						<param name="movie" value="http://www.youtube.com/watch/v/%s"></param>
						<param name="allowFullScreen" value="true"></param>
						<embed src="http://www.youtube.com/watch/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
						</object>
						""" % (video_id, video_id)
		
			# Url
		else:
			l = urlize(l)
		
		# Return
		output += l + " "
		
	return output