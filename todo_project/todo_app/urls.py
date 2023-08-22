from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IndexView, UserCreateView, MyLoginView, NotesListView, CreateNoteView, DeleteNoteView


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("auth/", MyLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("notes/", NotesListView.as_view(), name="notes"),
    path("add_note/", CreateNoteView.as_view(), name="add_note"),
    path("delete_note/<int:pk>/", DeleteNoteView.as_view(), name="delete_note"),
]
