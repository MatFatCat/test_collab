from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("my first Django App please dont stress me with excess files")