"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(jc(v@+#5pb*-w0p)xyupgtc7ec&9ta@s@+94%gy^2qk&dih5d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#允許條件:'*'-但代表所有的ip都能進來
ALLOWED_HOSTS = ['*']


# Application definition
# 應用程式要寫入
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'customer',
    'product',
    'contact',
    'photos',
    'cart',
    'sendmail',
    'war',
    'ukrayina',
    'russia',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'


#樣板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates').replace('\\','/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', #多媒體---這條屬於多媒體的 media資料夾

            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

#資料庫
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#
import pymysql  #預防動作
pymysql.install_as_MySQLdb() #預防動作



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web','USER':'root','PASSWORD':'123456789','HOST':'localhost','PORT':'3306',
    }
}








# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


#編譯語言                    zh-Hant:中文介面(t:繁體中文 s:簡體中文)
LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei' #

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

#根目錄新增
STATIC_ROOT =   os.path.join(BASE_DIR,'static')


#多媒體---url.py  新增---客戶端上傳照片,放置的地方
MEDIA_URL ='media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
 

STATICFILES_DIRS = (
    ("images",os.path.join(STATIC_ROOT,'images').replace('\\','/')),    
    ("js",os.path.join(STATIC_ROOT,'js').replace('\\','/')), 
    ("css",os.path.join(STATIC_ROOT,'css').replace('\\','/')), 
    ("vendors",os.path.join(STATIC_ROOT,'vendors').replace('\\','/')), 
    
    )

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
