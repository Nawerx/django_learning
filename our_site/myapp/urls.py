from django.urls import path

from .views import *

urlpatterns = [
    path("index/", index),
    path("show_int/<int:value>", show_int),
    path("show_str/<str:value>", show_str),
    path("show/", show),
]