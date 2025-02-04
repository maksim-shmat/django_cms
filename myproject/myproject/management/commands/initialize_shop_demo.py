import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils.translation import ugettext_lazy as _
try:
    import czipfile as zipfile
except ImportError:
    import zipfile


class Command(BaseCommand):
    help = _("Initialize the workdir to run the demo of myproject.")

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', '--no-input',
            action='store_false',
            dest='interactive',
            default=True,
            help="Do NOT prompt the user for input of any kind.",
        )

    def set_options(self, **options):
        self.interactive = options['interactive']


    def clear_compressor_cache(self):
        from django.core.cache import caches
        from django.core.cache.backends.base import InvalidCacheBackendError
        from compressor.conf import settings

        cache_dir = os.path.join(settings.STATIC_ROOT, settings.COMPRESS_OUTPUT_DIR)
        if settings.COMPRESS_ENABLED is False or not os.path.isdir(cache_dir) or os.listdir(cache_dir) != []:
            return
        try:
            caches['compressor'].clear()
        except InvalidCacheBackendError:
            pass

    def handle(self, verbosity, *args, **options):
        self.set_options(**options)
        self.clear_compressor_cache()
        call_command('migrate')
        initialize_file = os.path.join(settings.WORK_DIR, '.initialize')
        if os.path.isfile(initialize_file):
            self.stdout.write("Initializing project myproject")
            call_command('makemigrations', 'myproject')
            call_command('migrate')
            os.remove(initialize_file)
            call_command('loaddata', 'skeleton')
            call_command('shop', 'check-pages', add_recommended=True)
            call_command('assign_iconfonts')
            call_command('create_social_icons')
            call_command('download_workdir', interactive=self.interactive)
            call_command('loaddata', 'products-media')
            call_command('import_products')
            self.create_polymorphic_subcategories()
            call_command('initialize_inventories')
            try:
                call_command('sendcloud_import')
            except CommandError:
                pass
            try:
                call_command('search_index', action='rebuild', force=True)
            except:
                pass
        else:
            self.stdout.write("Project myproject already initialized")
            call_command('migrate')


    def create_polymorphic_subcategories(self):
        from cms.models.pagemodel import Page
        from shop.management.commands.shop import Command as ShopCommand
        from myproject.models import Commodity, SmartCard, SmartPhoneModel

        apphook = ShopCommand.get_installed_apphook('CatalogListCMSApp')
        catalog_pages = Page.objects.drafts().filter(
            application_urls=apphook.__class__.__name__)
        assert catalog_pages.count() == 1, "There should be only one catalog page"
        self.create_subcategory(
            apphook, catalog_pages.first(), "Earphones", Commodity)
        self.create_subcategory(
            apphook, catalog_pages.first(), "Smart Cards", SmartCard)
        self.create_subcategory(
            apphook, catalog_pages.first(), "Smart Phones", SmartPhoneModel)

    def create_subcategory(self, apphook, parent_page, title, product_type):
        from cms.api import create_page
        from cms.constants import TEMPLATE_INHERITANCE_MAGIC
        from cms.utils.i18n import get_public_languages
        from shop.management.commands.shop import Command as ShopCommand
        from shop.models.product import ProductModel
        from shop.models.related import ProductPageModel

        language = get_public_languages()[0]
        page = create_page(
            title,
            TEMPLATE_INHERITANCE_MAGIC,
            language,
            apphook=apphook,
            created_by="manage.py initialize_shop_demo",
            in_navigation=True,
            parent=parent_page,
        )
        ShopCommand.publish_in_all_languages(page)
        page = page.get_public_object()
        for product in ProductModel.objects.instance_of(product_type):
            ProductPageModel.objects.create(page=page, product=product)

