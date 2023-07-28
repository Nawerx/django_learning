from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Note, User


def index(request: HttpRequest):
    notes: Note = Note.objects.all()
    return render(request, "myapp/index.html", {"notes": notes})


def show_int(request: HttpRequest, value: int):
    return HttpResponse(f"INTValue = {value}")


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


