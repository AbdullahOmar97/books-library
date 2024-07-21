from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Book

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class BookListView(ListView):
    model = Book
    template_name = 'list_of_books.html'
    context_object_name = 'books'

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})