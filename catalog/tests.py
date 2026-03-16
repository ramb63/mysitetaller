from django.test import TestCase
from .models import Author, Book

class BookModelTest(TestCase):

    def test_create_book(self):

        author = Author.objects.create(name="Test")

        book = Book.objects.create(
            title="Book",
            author=author,
            isbn="1234567890"
        )

        self.assertTrue(book.is_available)