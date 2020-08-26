from .base import *

DEBUG = False

ADMINS = (
    ('Charles', 'ch4rles.co@gmail.com'),
)

ALLOWED_HOSTS = ['onlineedu.com', 'www.online.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'online_edu_db',
        'USER': 'postgres',
        'PASSWORD':"",
        'HOST': 'localhost',
        'PORT': '5432',
    }
}