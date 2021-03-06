"""
Django settings for house_inventory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(+sb__g4^ou)3i^zdj-a+u6xj6gkg+(glivv_^mfr-3)378co!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'house_inventory',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'house_inventory.urls'

WSGI_APPLICATION = 'house_inventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'



########################################################
########################################################
##"""
##Django settings for mysite project.
##
##For more information on this file, see
##https://docs.djangoproject.com/en/1.7/topics/settings/
##
##For the full list of settings and their values, see
##https://docs.djangoproject.com/en/1.7/ref/settings/
##"""
##
### Build paths inside the project like this: os.path.join(BASE_DIR, ...)
##import os
##BASE_DIR = os.path.dirname(os.path.dirname(__file__))
##
##
### Quick-start development settings - unsuitable for production
### See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
##
### SECURITY WARNING: keep the secret key used in production secret!
##SECRET_KEY = 'j)+jg9776z@o%!q&*7)=is_nxujf9*veky9+@4$b**%dp(&r-*'
##
### SECURITY WARNING: don't run with debug turned on in production!
##DEBUG = True
##
##TEMPLATE_DEBUG = True
##
##TEMPLATE_DIRS = (
##    #'C:/M-Drive/PRO7 - Software Solutions Guru/Technologies/Python/Django/mysite/mysite/templates',
##    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
##)
##ALLOWED_HOSTS = []
##
##
### Application definition
##
##INSTALLED_APPS = (
##    'django.contrib.admin',
##    'django.contrib.auth',
##    'django.contrib.contenttypes',
##    'django.contrib.sessions',
##    'django.contrib.messages',
##    'django.contrib.staticfiles',
##    'books',
##)
##
##MIDDLEWARE_CLASSES = (
##    'django.contrib.sessions.middleware.SessionMiddleware',
##    'django.middleware.common.CommonMiddleware',
##    'django.middleware.csrf.CsrfViewMiddleware',
##    'django.contrib.auth.middleware.AuthenticationMiddleware',
##    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
##    'django.contrib.messages.middleware.MessageMiddleware',
##    'django.middleware.clickjacking.XFrameOptionsMiddleware',
##)
##
##ROOT_URLCONF = 'mysite.urls'
##
##WSGI_APPLICATION = 'mysite.wsgi.application'
##
##
### Database
### https://docs.djangoproject.com/en/1.7/ref/settings/#databases
##
##DATABASES = {
##    'default': {
##        'ENGINE': 'django.db.backends.sqlite3',
##        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
##    }
##}
##
### Internationalization
### https://docs.djangoproject.com/en/1.7/topics/i18n/
##
##LANGUAGE_CODE = 'en-us'
##
##TIME_ZONE = 'UTC'
##
##USE_I18N = True
##
##USE_L10N = True
##
##USE_TZ = True
##
##
### Static files (CSS, JavaScript, Images)
### https://docs.djangoproject.com/en/1.7/howto/static-files/
##
##STATIC_URL = '/static/'








