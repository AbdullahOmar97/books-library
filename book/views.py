from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Book

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(ListView):
    model = Book
    template_name = 'list_of_books.html'
    context_object_name = 'books'