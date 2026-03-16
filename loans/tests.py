from django.test import TestCase
from django.contrib.auth.models import User
from catalog.models import Book
from .models import Loan

class LoanTest(TestCase):

    def test_create_loan(self):
        user = User.objects.create(username="test")
        book = Book.objects.create(title="Book", author="A", isbn="1")
        loan = Loan.objects.create(user=user, book=book)

        self.assertEqual(loan.book.title, "Book")