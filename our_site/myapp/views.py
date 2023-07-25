from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Note


def index(request: HttpRequest):
    notes: Note = Note.objects.all()
    return render(request, "myapp/index.html", {"notes": notes})


def show_int(request: HttpRequest, value: int):
    return HttpResponse(f"INTValue = {value}")


def show_str(request: HttpResponse, value: str):
    return HttpResponse(f"STRValue = {value=}")


def show(request: HttpResponse,):
    return HttpResponse("<h1>Tag h1</h1>")

