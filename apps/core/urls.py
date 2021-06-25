from django.urls import path, include
from .views import (
    Home,
)
# API urls
from apps.core.api import urls as apiurl

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("api/", include('apps.core.api.urls')),
]