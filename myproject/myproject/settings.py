"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from decimal import Decimal
import os
from django.urls import reverse_lazy
from django.utils.text import format_lazy
from django.utils.translation import ugettext_lazy as _
from cmsplugin_cascade.bootstrap4.mixins import BootstrapUtilities
from cmsplugin_cascade.extra_fields.config import PluginExtraFieldsConfig

SHOP_APP_LABEL = 'myproject'
BASE_DIR = os.path.dirname(__file__)

# Root directory for this django project
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))

# Directory where working files, such as media and databases are kept
WORK_DIR = os.environ.get('DJANGO_WORKDIR', os.path.abspath(
    os.path.join(PROJECT_ROOT, 'workdir')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = []

# SECURITY WARNING: in production, inject the secret key through the environment
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', '!!!SET DJANGO_SECRET_KEY!!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1   # 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'  # I'm set default from tutorial

USE_THOUSAND_SEPARATOR = True

# Application definition

# replace django.contrib.auth.models.User by implementation
# allowing to login via email address
AUTH_USER_MODEL = 'email_auth.User'

AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    'OPTIONS': {
        'min_length': 6,
    }
}]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'email_auth',
    'polymorphic',
    # deprecated: 'djangocms_admin_style',  # 1 but these (#?) for begin
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',    # 1
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'djangocms_text_ckeditor',  #13
    'django_select2',
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.segmentation',
    'cms_bootstrap',
    'adminsortable2',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_elasticsearch_dsl',
    'django_fsm',
    'fsm_admin',
    'djng',
    'cms',    # 1
    'menus',   # 1
    'treebeard',  # 1
    'compressor',
    'sass_processor',
    'sekizai',  # 3
    'django_filters',
    'filer',  #11
    'easy_thumbnails',  #11
    'easy_thumbnails.optimize',
    'parler',
    'post_office',
    'shop_paypal',
    'shop_stripe',
    'shop_sendcloud',
    'shop2',
    'myproject',
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shop2.middleware.CustomerMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',         #3
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',  # 3
    'cms.middleware.user.CurrentUserMiddleware',         # 3
    'cms.middleware.page.CurrentPageMiddleware',         # 3
    'cms.middleware.utils.ApphookReloadMiddleware',# 3 ? go up to head of list
    'cms.middleware.toolbar.ToolbarMiddleware',          # 3
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'djangoshop'),
        'USER': os.getenv('POSTGRES_USER', 'djangoshop'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WORK_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'en'  # 2 but without js
USE_I18N = True

LANGUAGES = ('en-us')  # 2

PARLER_DEFAULT_LANGUAGE = LANGUAGE_CODE

PARLER_LANGUAGES = {
        # Global site
        1: (
            {'code': 'en',},
            {'code': 'en-us',},
            {'code': 'be',},
        ),
        # US site
        2: (
            {'code': 'en-us',},
            {'code': 'en',},
        ),
        # Beralusian Kingdom site
        3: (
            {'code': 'be',},
            {'code': 'ru',},
        ),
        'default': {
            'fallbacks': ['en'],
            'hide_untrnslated': False,
        }
}

CMS_LANGUAGES = {
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
        'public': True,
        'code': '{{ language }}',
        'hide_untranslated': False,
        'name': '{{ language.title() }}',
        'redirect_on_fallback': True,
}
USE_I18N = False

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

X_FRAME_OPTIONS = 'SAMEORIGIN' # 4

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(WORK_DIR, 'media') # 9

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'  # 9

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', os.path.join(WORK_DIR, 'static'))

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    # or 'django.contrib.staticfiles.finders.FileSystemFinder',
    'myproject.finders.FileSystemFinder',
    # or 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'myproject.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    ('node_modules', os.path.join(PROJECT_ROOT, 'node_modules')),
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [],   # 9
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n', # 5
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',   # 3
            'cms.context_processors.cms_settings',  # 5
            'shop2.context_processors.customer',
            'shop2.context_processors.shop_settings',
            'shop_stripe.context_processors.public_keys',
        ]
    }
}, {
    'BACKEND': 'post_office.template.backends.post_office.PostOfficeTemplates',
    'APP_DIRS': True,
    'DIRS': [],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.request',
        ]
    }
}]

POST_OFFICE = {
    'TEMPLATE_ENGINE': 'post_office',
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'select2': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

############################################
# settings for caching and storing session data
REDIS_HOST = os.getenv('REDIS_HOST')
if REDIS_HOST:
    SESSION_ENGINE = 'redis_sessions.session'

    SESSION_REDIS = {
        'host': REDIS_HOST,
        'port': 6379,
        'db': 0,
        'prefix': 'session-',
        'socket_timeout': 1
    }

    CACHES['default'] = {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://{}:6379/1'.format(REDIS_HOST),
    }
    COMPRESS_CACHE_BACKEND = 'compressor'
    CACHES[COMPRESS_CACHE_BACKEND] = {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://{}:6379/2'.format(REDIS_HOST),
    }
    CACHE_MIDDLEWARE_ALIAS = 'default'
    CACHE_MIDDLEWARE_SECONDS = 3600
else:
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SESSION_SAVE_EVERY_REQUEST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'post_office': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

SILENCED_SYSTEM_CHECKS = ['auth.W004']

FIXTURE_DIRS = [
    os.path.join(WORK_DIR, 'fixtures'),
]

############################################
# settings for sending mail

EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', 25)
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_USER', 'no-reply@localhost')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_PASSWORD', 'smtp-secret')
EMAIL_USE_TLS = bool(os.getenv('DJANGO_EMAIL_USE_TLS', '1'))
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_EMAIL_FROM', 'no-reply@localhost')
EMAIL_REPLY_TO = os.getenv('DJANGO_EMAIL_REPLY_TO', 'info@localhost')
EMAIL_BACKEND = 'post_office.EmailBackend'


############################################
# settings for third party Django apps

NODE_MODULES_URL = STATIC_URL + 'node_modules/'

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_ROOT, 'node_modules'),
]

COERCE_DECIMAL_TO_STRING = True

FSM_ADMIN_FORCE_PERMIT = True

ROBOTS_META_TAGS = ('noindex', 'nofollow')

SERIALIZATION_MODULES = {'json': str('shop2.money.serializers')}

############################################
# settings for django-restframework and plugins

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'shop2.rest.money.JSONRenderer',
        # can be disabled for production environments
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 16,
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'shop2.serializers.auth.LoginSerializer',
}

############################################
# settings for storing files and images

FILER_ADMIN_ICON_SIZES = ('16', '32', '48', '80', '128')

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = False

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

THUMBNAIL_HIGH_RESOLUTION = False    #12

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_PROCESSORS = (    #12
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


############################################
# settings for django-cms and its plugins

CMS_TEMPLATES = [    # 7
    ('myproject/pages/default.html', ("Default Page"),("Default Page"))
]

CMS_CACHE_DURATIONS = {
    'content': 600,
    'menus': 3600,
    'permissions': 86400,
}

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'Breadcrumb': {
        'plugins': ['BreadcrumbPlugin'],
        'parent_classes': {'BreadcrumbPlugin': None},
    },
    'Commodity Details': {
        'plugins': ['BootstrapContainerPlugin', 'BootstrapJumbotronPlugin'],
        'parent_classes': {
            'BootstrapContainerPlugin': None,
            'BootstrapJumbotronPlugin': None,
        },
    },
    'Main Content': {
        'plugins': ['BootstrapContainerPlugin', 'BootstrapJumbotronPlugin'],
        'parent_classes': {
            'BootstrapContainerPlugin': None,
            'BootstrapJumbotronPlugin': None,
            'TextLinkPlugin': ['TextPlugin', 'AcceptConditionPlugin'],
        },
    },
    'Static Footer': {
        'plugins': ['BootstrapContainerPlugin', 'BootstrapJumbotronPlugin'],
        'parent_classes': {
            'BootstrapContainerPlugin': None,
            'BootstrapJumbotronPlugin': None,
        },
    },
}

CMSPLUGIN_CASCADE_PLUGINS = [
    'cmsplugin_cascade.bootstrap4',
    'cmsplugin_cascade.segmentation',
    'cmsplugin_cascade.generic',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.leaflet',
    'cmsplugin_cascade.link',
    'shop2.cascade',
]

CMSPLUGIN_CASCADE = {
    'link_plugin_classes': [
        'shop2.cascade.plugin_base.CatalogLinkPluginBase',
        'shop2.cascade.plugin_base.CatalogLinkForm',
    ],
    'alien_plugins': ['TextPlugin', 'TextLinkPlugin', 'AcceptConditionPlugin'],
    'bootstrap4': {
        'template_basedir': 'angular-ui/',
    },
    'plugins_with_extra_render_templates': {
        'CustomSnippetPlugin': [
            ('shop2/catalog/product-heading.html', _("Product Heading")),
            ('myproject/catalog/manufacturer-filter.html', _("Manufacturer Filter")),
        ],
        # required to purchase real estate
        'ShopAddToCartPlugin': [
            (None, _("Default")),
            ('myproject/catalog/commodity-add2cart.html', _("Add Commodity to Cart")),
        ],
    },
    'plugins_with_sharables': {
        'BootstrapImagePlugin': ['image_shapes', 'image_width_responsive', 'image_width_fixed',
                                 'image_height', 'resize_options'],
        'BootstrapPicturePlugin': ['image_shapes', 'responsive_heights', 'responsive_zoom', 'resize_options'],
    },
    'plugins_with_extra_fields': {
        'BootstrapCardPlugin': PluginExtraFieldsConfig(),
        'BootstrapCardHeaderPlugin': PluginExtraFieldsConfig(),
        'BootstrapCardBodyPlugin': PluginExtraFieldsConfig(),
        'BootstrapCardFooterPlugin': PluginExtraFieldsConfig(),
        'SimpleIconPlugin': PluginExtraFieldsConfig(),
    },
    'plugins_with_extra_mixins': {
        'BootstrapContainerPlugin': BootstrapUtilities(),
        'BootstrapRowPlugin': BootstrapUtilities(BootstrapUtilities.paddings),
        'BootstrapYoutubePlugin': BootstrapUtilities(BootstrapUtilities.margins),
        'BootstrapButtonPlugin': BootstrapUtilities(BootstrapUtilities.floats),
    },
    'leaflet': {
        'tilesURL': 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
        'accessToken': 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw',
        'apiKey': 'AIzaSyD71sHrtkZMnLqTbgRmY_NsO0A9l9BQmv4',
    },
    'bookmark_prefix': '/',
    'segmentation_mixins': [
        ('shop2.cascade.segmentation.EmulateCustomerModelMixin',
         'shop2.cascade.segmentation.EmulateCustomerAdminMixin'),
    ],
    'allow_plugin_hiding': True,
    'register_page_editor': True,
}

CKEDITOR_SETTINGS = {
    'language': 'en',    # en dumb
    'skin': 'moono-lisa',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        '/',
        ['Bold', 'Italic', 'Underline', 'Strike', '-',
            'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
        ['Table', 'Source']
    ],
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texteditor_config')),
}

CKEDITOR_SETTINGS_CAPTION = {
    'language': 'en',    # en dumb
    'skin': 'moono-lisa',
    'height': 70,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['Source']
    ],
}

CKEDITOR_SETTINGS_DESCRIPTION = {
    'language': 'en',  # set 'en' because dumb
    'skin': 'moono-lisa',
    'height': 250,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript',
            'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
        ['Source']
    ],
}

SELECT2_CSS = 'node_modules/select2/dist/css/select2.min.css'
SELECT2_JS = 'node_modules/select2/dist/js/select2.min.js'
SELECT2_I18N_PATH = 'node_modules/select2/dist/js/i18n'



#############################################
# settings for full index text search 

ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': '{}:9200'.format(ELASTICSEARCH_HOST)
    },
}


############################################
# settings for django-shop and its plugins

SHOP_VALUE_ADDED_TAX = Decimal(19)
SHOP_DEFAULT_CURRENCY = 'EUR'
SHOP_EDITCART_NG_MODEL_OPTIONS = "{updateOn: 'default blur', debounce: {'default': 2500, 'blur': 0}}"

SHOP_CART_MODIFIERS = [
    'myproject.modifiers.PrimaryCartModifier',
    'shop2.modifiers.defaults.DefaultCartModifier',
    'shop2.modifiers.taxes.CartExcludedTaxModifier',
    'myproject.modifiers.PostalShippingModifier',
    'shop_paypal.modifiers.PaymentModifier',
    'myproject.modifiers.StripePaymentModifier',
    'shop2.payment.modifiers.PayInAdvanceModifier',
    'shop2.modifiers.SendcloudShippingModifiers',
    'shop2.modifiers.defaults.WeightedCartModifier',
    'shop2.shipping.modifiers.SelfCollectionModifier',
]

SHOP_ORDER_WORKFLOWS = [
    'shop2.payment.workflows.ManualPaymentWorkflowMixin',
    'shop2.payment.workflows.CancelOrderWorkflowMixin',
    'shop2.shipping.workflows.PartialDeliveryWorkflowMixin',
    'shop2.shipping.workflows.CommissionGoodsWorkflowMixin',
    'shop2.shipping.workflows.SimpleShippingWorkflowMixin',
    'shop_paypal.payment.OrderWorkflowMixin',
    'shop_stripe.workflows.OrderWorkflowMixin',
]

SHOP_PAYPAL = {
    'API_ENDPOINT': 'https://api.sandbox.paypal.com',
    'MODE': 'sandbox',
    'CLIENT_ID': os.getenv('PAYPAL_CLIENT_ID'),
    'CLIENT_SECRET': os.getenv('PAYPAL_CLIENT_SECRET'),
    'PURCHASE_DESCRIPTION': _("Thanks for purchasing at "),
}

SHOP_STRIPE = {
    'PUBKEY': os.getenv('STRIPE_PUBKEY', 'pk_test_HlEp5oZyPonE21svenqowhXp'),
    'APIKEY': os.getenv('STRIPE_APIKEY', 'sk_test_xUdHLeFasmOUDvmke4DHGRDP'),
    'PURCHASE_DESCRIPTION': _("Thanks for purchasing at "),
}

SHOP_STRIPE_PREFILL = True

SHOP_SENDCLOUD = {
    'API_KEY': os.getenv('SENDCLOUD_PUBLIC_KEY'),
    'API_SECRET': os.getenv('SENDCLOUD_SECRET_KEY'),
}

SHOP_CASCADE_FORMS = {
    'CustomerForm': 'myproject.forms.CustomerForm',
}
