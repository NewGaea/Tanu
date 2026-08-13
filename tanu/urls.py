"""URL configuration for Tanu."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

handler404 = "core.views.not_found"
handler500 = "core.views.server_error"
