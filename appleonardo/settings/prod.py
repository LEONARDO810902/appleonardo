from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['leonardomerchan.com.co', 'cpanel6-co.conexcol.net']

ALLOWED_HOSTS = ['leonardomerchan.com.co', 'https://www.leonardomerchan.com.co/', 'http://www.leonardomerchan.com.co/', 'https://leonardomerchan.com.co/admin']

CSRF_TRUSTED_ORIGINS = ['https://leonardomerchan.com.co']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DBNAME_PRO'),
        'USER': get_secret('DBUSER_PRO'),
        'PASSWORD': get_secret('DBPASSWORD_PRO'),
        'HOST': 'localhost',
        'PORT_PRO': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = f'{BASE_DIR}{STATIC_URL}'
STATICFILES_URL = '/staticfiles/'
STATICFILES_DIRS = [f'{BASE_DIR}{STATICFILES_URL}',]


''' se cambia la carpeta de static a staticfiles corre el comando python manage.py collectstatic'''