""" Docs. """
import os
import logging
from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class myprojectName(AppConfig):
    """ docs. """
    name = 'myproject'
    verbose_name = _("My Shop")
    logger = logging.getLogger('myproject')

    def ready(self):
        if not os.path.isdir(settings.STATIC_ROOT):
            os.makedirs(settings.STATIC_ROOT)
        if not os.path.isdir(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        if hasattr(settings, 'COMPRESS_ROOT') and not os.path.isdir(settings.COMPRESS_ROOT):
            os.makedirs(settings.COMPRESS_ROOT)
        self.logger.info("Running as {{ cookiecutter.products_model }}{}".format(as_i18n))
        from myproject import search_indexes
        __all__ = ['search_indexes']
