from django.shortcuts import render
from django.http import HttpResponse

# Vistas sobre la aplicación de libros
def init(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


# vistas sobre el CRUD de libros
def books(request):
    return render(request, 'books/index.html')

def create(request):
    return render(request, 'books/create.html')

def update(request):
    return render(request, 'books/update.html')