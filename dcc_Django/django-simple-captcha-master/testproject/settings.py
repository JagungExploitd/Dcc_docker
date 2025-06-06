import os
import sys


SITE_ID = 1

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

PYTHON_VERSION = "%s.%s" % sys.version_info[:2]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_PATH, "django-simple-captcha.db"),
    }
}

# TEST_DATABASE_CHARSET = "utf8"
# TEST_DATABASE_COLLATION = "utf8_general_ci"

DATABASE_SUPPORTS_TRANSACTIONS = True

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.forms",
    "django.contrib.messages",
    # "rest_framework",
    "captcha",
]
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", "English"),
    # ('ja', u('日本語')),
)

FIXTURE_DIRS = (os.path.join(PROJECT_PATH, "fixtures"),)

ROOT_URLCONF = "testproject.urls"

DEBUG = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": False,
            "context_processors": (
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ),
        },
        "DIRS": ("templates",),
    }
]

USE_TZ = True
SECRET_KEY = "empty"
MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)


CAPTCHA_FLITE_PATH = os.environ.get("CAPTCHA_FLITE_PATH", None)
CAPTCHA_SOX_PATH = os.environ.get("CAPTCHA_SOX_PATH", None)
CAPTCHA_BACKGROUND_COLOR = "transparent"
CAPTCHA_LETTER_COLOR_FUNCT = "captcha.helpers.random_letter_color_challenge"
CAPTCHA_BACKGROUND_COLOR = "#ffffff"

ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1"]
