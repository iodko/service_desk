from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)
