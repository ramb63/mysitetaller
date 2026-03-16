from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"

    def clean_isbn(self):

        isbn = self.cleaned_data["isbn"]

        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must contain only numbers")

        if len(isbn) not in [10, 13]:
            raise forms.ValidationError("Invalid ISBN length")

        return isbn