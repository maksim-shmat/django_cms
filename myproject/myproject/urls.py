""" Docs. """

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include  # 6
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from cms.sitemaps import CMSSitemap
from myproject.sitemap import ProductSitemap

sitemaps = {'cmspages': CMSSitemap,
            'products': ProductSitemap}


def render_robots(request):
    permission = 'noindex' in settings.ROBOTS_META_TAGS and 'Disallow' or 'Allow'
    return HttpResponse('User-Agent: *\n%s: /\n' % permission, content_type='text/plain')


i18n_urls = (    # 6 but with urlpatterns from i18
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cms.urls')),
)
urlpatterns = [
    url(r'^robots\.txt$', render_robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^shop2/', include('shop2.urls')),
]
if settings.USE_I18N:
    urlpatterns.extend(i18n_patterns(*i18n_urls))
else:
    urlpatterns.extend(i18n_urls)
urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
