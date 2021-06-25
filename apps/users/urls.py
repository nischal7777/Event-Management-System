from django.urls import path
from .views import (
    AdminPanel
)

urlpatterns = [
    path("root/",AdminPanel.as_view(), name='root')
]
