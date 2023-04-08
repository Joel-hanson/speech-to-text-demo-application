import os
from pathlib import Path

from decouple import Csv, config


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# debug configures the dev and production setup, False means the project runs in production mode and True means project runs in development mode.
DEBUG = config("DEBUG", default=True, cast=bool)

if DEBUG:
    from fnmatch import fnmatch

    class pattern_list(list):
        def __contains__(self, key):
            for pattern in self:
                if fnmatch(key, pattern):
                    return True
            return False

    INTERNAL_IPS = pattern_list(["127.0.0.1", "192.168.*.*"])
    print(INTERNAL_IPS)
else:
    INTERNAL_IPS = config("INTERNAL_IPS", cast=Csv())

# Allowed hosts is the list of hosts to allow hitting the project.
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Needed for 'debug' to be available inside templates.
# See https://docs.djangoproject.com/en/4.1/ref/templates/api/#django-template-context-processors-debug

# The django apps and the external apps.
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [base_dir_join("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Vite App Dir: point it to the folder your vite app is in.
VITE_APP_DIR = base_dir_join("frontend")

# Storage
STATIC_ROOT = base_dir_join("staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    VITE_APP_DIR + "/dist",
]

MEDIA_ROOT = base_dir_join("mediafiles")
MEDIA_URL = "/media/"

# SSL
# SECURE_PROXY_SSL_HEADER = config('SECURE_PROXY_SSL_HEADER', cast=Csv(post_process=tuple))

# REST framework configuration.
REST_FRAMEWORK = {"TEST_REQUEST_DEFAULT_FORMAT": "json"}
