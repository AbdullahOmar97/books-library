from django.urls import path
from .views import HomePageView, BookListView, book_detail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]
