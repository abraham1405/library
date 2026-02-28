from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.init, name='init'),
    path('about', views.about, name='about'),
    path('books', views.books, name='books'),
    path('books/create', views.create, name='create'),
    path('books/update/', views.update, name='update'),
    path('books/update/<int:id>', views.update, name='update'),
    path('books/delete/<int:id>', views.delete, name='delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
