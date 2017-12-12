"""
Django settings for energysoft project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGES_ROOT='media/images/'
VIDEOS_ROOT='media/videos/'
DOCUMENT_ROOT='media/document/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w7+!$ej12yys+=d!ohstg5gggwx3c=a@+)hrw7a^k24p_42iz4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.0.0.15','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'embed_video',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'master', #custom app
    'employee', #custom app
    'events', #custom app
    'news', #custom app
    'gallery', #custom app
    'shoutout', #custom app
    'feedback', #custom app
    'livetelecast', #custom app 
    'rest_framework', #predefined app  
    'rest_framework.authtoken', #predefined app
    # 'oauth2_provider', #predefined app
    # 'corsheaders',
    'energysoft_api', #custom app 
    'haystack', #predefined app,
    'multiupload', #custom app 
    'rest_auth' #predefined app,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'energysoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR,'templates/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# import os.path
# print "os_path"+os.path.join(BASE_DIR,'templates/')
# print os.path.exists('/home/deepak/django_projects/nergyso_web/energysoft/energysoft/templates/search/indexes/events/events_text.txt')


WSGI_APPLICATION = 'energysoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'energysoft', 
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    # 'DEFAULT_PAGINATION_CLASS':[ 
    #     'rest_framework.pagination.LimitOffsetPagination'
    # ],
    # 'DEFAULT_RENDERER_CLASSES': [
    #     # 'rest_framework.renderers.XMLRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication',
    # ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    # 'PAGE_SIZE': 100
}

# CORS_ORIGIN_ALLOW_ALL = True

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'localhost:9200',
        'INDEX_NAME': 'haystack',
    },
}

# MEDIA_ROOT = os.path.join(BASE_DIR,'media/')

# IMAGES_ROOT = MEDIA_ROOT + "images"

# VIDEOS_ROOT = MEDIA_ROOT + "videos"

# DOCUMENT_ROOT = MEDIA_ROOT + "document"

SITE_ID = 1

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True   
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kalaimca.gs@gmail.com'
EMAIL_HOST_PASSWORD = 'kalai123'

#to use old_password
OLD_PASSWORD_FIELD_ENABLED = True

#to keep the user logged in after password change
LOGOUT_ON_PASSWORD_CHANGE = False
