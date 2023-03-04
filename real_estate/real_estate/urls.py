from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from listings.views import listings_list,listing_retrive,listing_create,listing_update,delete_listing

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",listings_list),
    path("listing/<pk>/",listing_retrive),
    path("add-listing/",listing_create),
    path("listing/<pk>/edit/",listing_update),
    path("listing/<pk>/delete/",delete_listing)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 