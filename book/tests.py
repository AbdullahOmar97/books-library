from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class BookListTests(TestCase):
    def test_book_list_page_status_code(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_page_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, 'list_of_books.html')
