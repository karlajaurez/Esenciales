from django.conf.urls import url
from django.contrib.auth import views
from home.views import ProductoView
# Static files
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^productos$', ProductoView.as_view(), name='productos'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
