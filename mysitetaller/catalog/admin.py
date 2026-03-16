from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "isbn", "is_available")

    search_fields = ("title", "isbn")

    list_filter = ("is_available",)