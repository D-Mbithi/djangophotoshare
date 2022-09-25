from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

from photos.views import home

urlpatterns = [
    path('', home, name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('', include('photos.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)