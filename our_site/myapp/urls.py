from django.urls import path

from .views import *

urlpatterns = [
    path("notes/", NotesListview.as_view()),
    path("show_int/<int:value>", show_int),
    path("show_str/<str:value>", show_str),
    path("show/", show),
    path("notes/<int:id>", NoteView.as_view(), name='show_note'),
    path("users/<int:id>", show_user, name='show_user'),
    path("create_note/", NoteCreateView.as_view(), name="create_note"),
    path("update_note/<int:pk>", NoteUpdateView.as_view(), name="update_note")
]