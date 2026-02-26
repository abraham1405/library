from django.shortcuts import render
from django.http import HttpResponse


def init(request):
    return HttpResponse("<h1>¡Bienvenido July!</h1>")

def home(request):
    return render()