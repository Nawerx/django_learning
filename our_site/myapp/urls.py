from django.urls import path

from .views import *

urlpatterns = [
    path("notes/", Notes_list_view.as_view()),
    path("show_int/<int:value>", show_int),
    path("show_str/<str:value>", show_str),
    path("show/", show),
    path("notes/<int:id>", Note_view.as_view(), name='show_note'),
    path("users/<int:id>", show_user, name='show_user'),
    path("create_note/", show_form, name="create_note")
]