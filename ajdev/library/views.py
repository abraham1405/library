from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Vistas sobre la aplicación de libros
def init(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


# vistas sobre el CRUD de libros
def books(request):
    listBooks = Book.objects.all()
    return render(request, 'books/index.html', {'listBooks': listBooks})

def create(request):
    formulary = BookForm(request.POST or None, request.FILES or None)
    if formulary.is_valid():
        formulary.save()
        return redirect('books')
    return render(request, 'books/create.html', {'formulary': formulary})

def update(request, id):
    book = Book.objects.get(id=id)
    formulay = BookForm(request.POST or None, request.FILES or None, instance=book)
    if formulay.is_valid() and request.POST :
        formulay.save()
        return redirect('books')
    return render(request, 'books/update.html', {'formulary': formulay})

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')