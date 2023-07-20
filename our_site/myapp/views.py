from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("<h1>Hello World</h1>")


def show_int(request: HttpRequest, value: int):
    return HttpResponse(f"INTValue = {value}")


def show_str(request: HttpResponse, value: str):
    return HttpResponse(f"STRValue = {value=}")


def show(request: HttpResponse,):
    return HttpResponse("<h1>Tag h1</h1>")