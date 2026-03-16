from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from django.db.models import Q


def book_list(request):

    query = request.GET.get("q")

    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query)
        )

    paginator = Paginator(books, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "catalog/book_list.html", {
        "page_obj": page_obj
    })