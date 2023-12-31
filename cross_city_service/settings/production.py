"""
Django settings for cross_city_service project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# DB constants
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['cross-city-taxi.ru', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'rest_framework',
    'orders.apps.OrdersConfig',
    'drivers.apps.DriversConfig',
    'staff.apps.StaffConfig',
    'tariffs.apps.TariffsConfig',
    'api.apps.ApiConfig',
    'cities.apps.CitiesConfig',
    'feedback.apps.FeedbackConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'cross_city_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cross_city_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
        # 'PORT': '5433',
    },
}

# db = dj_database_url.config()
# DATABASES['default'].update(db)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'  # 'en-us'  'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# -------------------------------------------------------- static settings
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# здесь мы указываем откуда будем доставать статику и подключать к шаблону,
# с помощью тега {% static 'css/style.css' %}
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
STATICFILES_DIRS = ['/app/staticfiles', ]

# здесь мы указываем куда django будет собирать всю статику проекта при команде collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# -------------------------------------------------------- static settings

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------- for django debug toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html

# INTERNAL_IPS = ('127.0.0.1',)

# -------------------------------------------------------- for media
# MEDIA_URL = '/images/'

# путь в файловой системе, где эти файлы будут храниться

MEDIA_ROOT = '/app/media/'

MEDIA_URL = '/media/'

# -------------------------------------------------------- for CORS
# SECURE_CROSS_ORIGIN_OPENER_POLICY = None
CORS_ALLOWED_ORIGINS = ['http://cross-city-taxi.ru',
                        'http://localhost', 'http://cross-city-taxi.ru']
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ALLOW_ALL_ORIGINS = DEBUG
"""
# -----------------------------------------------------------DB postgres

DB_NAME = os.environ.get('DB_NAME')  # crosscitytest
DB_USER = os.environ.get('DB_USER')  # postgres
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')  # 127.0.0.1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# -----------------------------------------------------------DB postgres
"""
