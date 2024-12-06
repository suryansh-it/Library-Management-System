from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields= ['title', 'authors', 'isbn', 'borrower', 'is_available', 'additional_info']