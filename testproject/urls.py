from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include


admin.autodiscover()


urlpatterns = []
urlpatterns += i18n_patterns(
    path(
        'admin/',
        admin.site.urls
    ),
    url(
        r'^',
        include('cms.urls')
    ),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
