from django.urls import path

from .views import *

urlpatterns = [
    path("index/", index),
    path("show_int/<int:value>", show_int),
    path("show_str/<str:value>", show_str),
    path("show/", show),
    path("notes/<int:id>", show_note, name='show_note'),
    path("users/<int:id>", show_user, name='show_user')
]