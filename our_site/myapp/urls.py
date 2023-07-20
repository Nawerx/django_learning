from django.urls import path

from .views import *

urlpatterns = [
    path("index/", index),
    path("show_int/<int:value>", show_int),
]