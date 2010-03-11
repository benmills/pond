import mongoengine
mongoengine.connect('console')

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
PATH = '/sites/console/'

SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = PATH+'media'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'
SECRET_KEY = '2l6-a0h-3bs#a14v**#puc+z=2k#94hyx&=ahbvhl=vj(pi1q@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'console.urls'

TEMPLATE_DIRS = (PATH+'templates/')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
		'chat',
)
