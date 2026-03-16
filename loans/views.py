from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Loan


@login_required
def my_loans(request):

    loans = Loan.objects.filter(
        user=request.user,
        is_active=True
    )

    return render(request, "loans/my_loans.html", {
        "loans": loans
    })