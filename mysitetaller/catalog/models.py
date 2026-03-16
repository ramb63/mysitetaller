from django.db import models

from mysitetaller.loans.models import Loan


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)
    
class Fine(models.Model):

    loan = models.OneToOneField(Loan, on_delete=models.CASCADE)

    late_days = models.IntegerField()

    fine_amount = models.IntegerField()

    def __str__(self):
        return f"Fine {self.fine_amount}"
    
    def __str__(self):
        return self.title