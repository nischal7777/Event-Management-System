from django.urls import path
from .views import (
    BookDay
)

urlpatterns = [
    path("book/", BookDay.as_view(), name="book"),
]
