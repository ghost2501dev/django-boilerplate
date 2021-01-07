import os
import sys

import environ

from django.utils.translation import gettext_lazy as _

base_dir = environ.Path(__file__) - 3
live_dir = base_dir.path('.live')

PROJECT_ALIAS = 'project'
PROJECT_DISPLAY_NAME = 'Project'

# Defaults
env = environ.Env(
    DEBUG=(bool, False),
    EMAIL_BACKEND=(str, 'django.core.mail.backends.smtp.EmailBackend'),
    EMAIL_HOST=(str, 'localhost'),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    EMAIL_PORT=(int, 25),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_USE_SSL=(bool, False),
    SERVER_EMAIL=(str, 'root@localhost'),
    DEFAULT_FROM_EMAIL=(str, 'info@localhost'),
    EMAIL_SUBJECT_PREFIX=(str, PROJECT_DISPLAY_NAME),
    DATABASE_HOST=(str, 'localhost'),
    DATABASE_PORT=(str, ''),
    DATABASE_MAX_CONNS=(int, 20),
    ADMINS=(list, []),
    SHOW_DEBUG_TOOLBAR=(bool, False),
    LOAD_EXTERNAL_REFS=(bool, True),
)

environ.Env.read_env(base_dir('.env'))
sys.path.append(base_dir('apps'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = (
    '127.0.0.1',
    '0.0.0.0',
)
SITE_ID = 1

# Follow this convention, but ignore in corner cases:
# 1. Django
# 2. Debug/testing
# 3. Third party
# 4. Local
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'hijack',
    'compat',

    'corsheaders',
    'parler',
    'sekizai',

    'users',
    'common',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# =============================================================================
# Templates
# =============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            base_dir('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
            'debug': DEBUG,
        },
    },
]

ALLOWABLE_TEMPLATE_SETTINGS = ('DEBUG', 'LOAD_EXTERNAL_REFS', 'PROJECT_DISPLAY_NAME')

HTML_MINIFY = not DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda req: (
        req.environ.get('SERVER_NAME', None) != 'testserver' and
        req.META.get('REMOTE_ADDR', None) in INTERNAL_IPS and
        DEBUG and
        env('SHOW_DEBUG_TOOLBAR')
    ),
}


# =============================================================================
# Database
# =============================================================================

# CONN_MAX_AGE must be set to 0, or connections will never go back to the pool
DATABASES = {
    'default': {
        'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 0,
        'OPTIONS': {
            'MAX_CONNS': env('DATABASE_MAX_CONNS'),
        },
    }
}


# =============================================================================
# Auth
# =============================================================================

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

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'


# =============================================================================
# i18n/l10n
# =============================================================================

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
]

LOCALE_PATHS = [base_dir('locale')]

PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'en',},
    ),
}


# =============================================================================
# Static and media
# =============================================================================

STATICFILES_DIRS = [
    base_dir('static'),
]

STATIC_ROOT = live_dir('static')
STATIC_URL = '/static/'

MEDIA_ROOT = live_dir('media')
MEDIA_URL = '/media/'

if not DEBUG:
    # Add WhiteNoiseMiddleware immediately after SecurityMiddleware.
    # Avoid using whitenoise. Configure a server to provide static.
    # Use whitenoise only in corner cases or for debugging purposes.
    index = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
    MIDDLEWARE.insert(index + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')

LOAD_EXTERNAL_REFS = env('LOAD_EXTERNAL_REFS')


# =============================================================================
# Mailing
# =============================================================================

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_USE_SSL = env('EMAIL_USE_SSL')
SERVER_EMAIL = env('SERVER_EMAIL')  # Email to send error messages
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX')


# =============================================================================
# Caches
# =============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# =============================================================================
# Hijack
# =============================================================================

HIJACK_LOGIN_REDIRECT_URL = '/admin/'
HIJACK_LOGOUT_REDIRECT_URL = HIJACK_LOGIN_REDIRECT_URL
HIJACK_ALLOW_GET_REQUESTS = True


# =============================================================================
# Fixtures
# =============================================================================

FIXTURE_DIRS = [
    base_dir('fixtures'),
]


# See apps/common/management/commands/pushfixtures.py
FIXTURES = [
#    'file.json',
]


# =============================================================================
# Others
# =============================================================================

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

ADMINS = []
admins = env('ADMINS')
for admin in admins:
    ADMINS.append(admin.split(':'))
