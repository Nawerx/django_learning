from typing import Any
from .forms import CreateNoteForm
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Note, User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request: HttpRequest):
    args = request.POST
    return HttpResponse(escape(str(dict((args)))))
    # notes: Note = Note.objects.all()
    # return render(request, "myapp/index.html", {"notes": notes})


def show_form(request: HttpRequest):
    if request.method == "GET":
        form = CreateNoteForm()

    elif request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            note = form.save()

        return redirect(note.get_absolute_url())

    return render(request=request, template_name="myapp/note_form.html", context={"form": form})


def show_int(request: HttpRequest, value: int):
    return HttpResponse(f"INTValue = {value}")


class Notes_list_view(ListView):
    model = Note
    template_name = "myapp/index.html"
    context_object_name = "notes"


class Note_view(DetailView):
    model = Note
    template_name = "myapp/note.html"
    pk_url_kwarg = "id"



def show_str(request: HttpResponse, value: str):
    return HttpResponse(f"STRValue = {value=}")


def show(request: HttpResponse):
    return HttpResponse("<h1>Tag h1</h1>")


def show_note(requset: HttpResponse, id: int):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return(HttpResponse(f"Не існує записки з айди {id}"))

    return HttpResponse(f"<h1>{note.title} {note.content} </h1>")


def show_user(requset: HttpResponse, id: int):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return(HttpResponse(f"Не існує користувача з айди {id}"))

    return HttpResponse(f"<h1>{user.name} {user.email} </h1>")


