from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tibpljeo)1)h86!5#76m#gnhc&ry#aq@p28of!3ylw38=n-3a0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_project',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'db-svc',
        'PORT': 3306,
    }
}
