import os
from .base import *


DEBUG = False


ALLOWED_HOSTS = ['marketasynkova.cz', 'www.marketasynkova.cz']



CORS_ALLOWED_ORIGINS = [
    "https://marketasynkova.cz",
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



LOGGING = {                                                                                                                 
            'version': 1,
                'disable_existing_loggers': False,
                    'handlers': {
                                'logfile': {
                                                'class': 'logging.FileHandler',
                                                            'filename': '../logs/django_server.log',
                                                                    },
                                    },
                        'loggers': {
                                    'django': {
                                                    'handlers': ['logfile'],
                                                            },
                                        },
                        }

