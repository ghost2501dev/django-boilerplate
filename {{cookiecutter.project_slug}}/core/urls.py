import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

from common.views import (
    bad_request, page_not_found, permission_denied, server_error,
    simulated_error, change_language,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('hijack/', include('hijack.urls')),
    path('simulated-error/', simulated_error),
    path('change-language/', change_language, name='change-language'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('error400/', bad_request),
        path('error403/', permission_denied),
        path('error404/', page_not_found),
        path('error500/', server_error),
    ]

admin.site.site_header = settings.PROJECT_DISPLAY_NAME

handler400 = 'common.views.bad_request'
handler403 = 'common.views.permission_denied'
handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'
