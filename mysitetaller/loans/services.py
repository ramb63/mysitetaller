from django.db import transaction
from datetime import date
from .models import Loan, Fine


@transaction.atomic
def create_loan(book, user, due_date):

    if not book.is_available:
        raise ValueError("Book already loaned")

    loan = Loan.objects.create(
        book=book,
        user=user,
        due_date=due_date
    )

    book.is_available = False
    book.save()
    return loan
def return_book(loan):

    loan.end_date = date.today()
    loan.is_active = False
    loan.save()

    book = loan.book
    book.is_available = True
    book.save()

    late_days = (loan.end_date - loan.due_date).days

    if late_days > 0:
        Fine.objects.create(
            loan=loan,
            late_days=late_days,
            fine_amount=late_days * 1000
        )   
    

    return loan
