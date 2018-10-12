from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myproject.core.urls')),
    path('accounts/', include('myproject.accounts.urls')),
    path('api/crm/', include('myproject.crm.urls')),
    # path('crm/', include('myproject.crm.urls')),
    path('financial/', include('myproject.financial.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
