from django.urls import path

from .views import HomeView, health

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("healthz/", health, name="health"),
]
