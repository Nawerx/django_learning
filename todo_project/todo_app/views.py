from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .forms import UserCreateForm, LoginUserForm, NoteForm
from django.urls import reverse_lazy
from .models import Note

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLoginView(LoginView):
    template_name = "todo_app/login.html"
    redirect_authenticated_user = True
    form_class = LoginUserForm

    def get_success_url(self) -> str:
        return reverse_lazy("home")


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "todo_app/index.html"


class UserCreateView(CreateView):
    template_name = "todo_app/signup.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("home")


class NotesListView(LoginRequiredMixin, ListView):
    template_name = "todo_app/notes.html"
    model = Note
    context_object_name = "notes"

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(author=self.request.user).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NoteForm()
        return context


class CreateNoteView(CreateView):
    template_name = "todo_app/notes.html"
    form_class = NoteForm
    success_url = reverse_lazy("notes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def title_valid(self, title):
    #     print(title)
    #     if "!" in title:
    #         print("! in title")
    #     return super().title_valid(title)

class DeleteNoteView(DeleteView):
    template_name = "todo_app/notes.html"
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes")

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)