from django.db import models
from django.contrib.auth.models import User
from catalog.models import Book

class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    end_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book} - {self.user}"