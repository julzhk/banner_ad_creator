from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from bannerResult.views import process_submission, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('bannerForm/', include('bannerForm.urls')),
    path('bannerResult/', include('bannerResult.urls')),
    path('htmx/', views.htmx_home, name='htmx'),
    path('admin/', admin.site.urls),
    path('process_submission/', process_submission, name='process_submission'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
