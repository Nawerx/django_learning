from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpResponse):
    return HttpResponse("<h1>Hello World</h1>")


def show_int(request: HttpResponse, value: int):
    return HttpResponse(f"Value = {value}")
