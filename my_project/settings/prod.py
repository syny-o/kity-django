import os
from .base import *


DEBUG = False


ALLOWED_HOSTS = ['filateliestafl.eu', 'www.filateliestafl.eu']



CORS_ALLOWED_ORIGINS = [
    "https://filateliestafl.eu",
]

CSRF_TRUSTED_ORIGINS = [*CORS_ALLOWED_ORIGINS]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_one',
        'USER': 'user_one',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}

