from django.urls import path
from .views import HomePageView, BookListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
]
