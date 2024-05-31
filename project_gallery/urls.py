from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from gallery import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.gallery_view, name="main"),
    path("image/<int:pk>/", views.image_detail, name="image_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
