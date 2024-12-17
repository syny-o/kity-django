import os
from .base import *


DEBUG = True


ALLOWED_HOSTS = ["localhost",]


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
CSRF_TRUSTED_ORIGINS = [*CORS_ALLOWED_ORIGINS]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

