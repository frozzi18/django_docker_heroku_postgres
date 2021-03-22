#
#   These are the settings for a Travis Integrating Testing Environments
#

from .common import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

ALLOWED_HOSTS = ['localhost']
SECRET_KEY = '=5y-up0zi2^szvua1c_bxn!#*kwgv=tuap1c99du4x^uho6k_)'
STATIC_URL = '/static/'

DEBUG = True

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }