from django.conf.urls.defaults import *
from datetime import datetime, date, timedelta
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'chat.views.index', name='index'),
	url(r'^post/$', 'chat.views.post_chat', name='post'),
	url(r'^check$', 'chat.views.check_chat', name='check_chat'),
	url(r'^feed/$', 'chat.views.get_chat', name='get_chat'),
	url(r'^feed/(?P<date>.*)$', 'chat.views.get_chat', name='get_chat'),
	url(r'^feed.json$', 'chat.views.get_chat_json', name='get_chat_json'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
