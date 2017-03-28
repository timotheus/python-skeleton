from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # url(r'^$', views.main),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
