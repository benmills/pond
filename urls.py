from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'commandlines.views.index', name='index'),
	url(r'^post/$', 'commandlines.views.post_chat', name='post'),
	url(r'^check/$', 'commandlines.views.check_chat', name='check_chat'),
	url(r'^feed/$', 'commandlines.views.get_chat', name='get_chat'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
