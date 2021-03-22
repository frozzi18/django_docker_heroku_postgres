"""
Setting for local environment
"""

from .common import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=5y-up0zi2^szvua1c_bxn!#*kwgv=tuap1c99du4x^uho6k_)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_postgress_docker_db',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': ''
    }
}



DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        'rest_framework.renderers.BrowsableAPIRenderer',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}

