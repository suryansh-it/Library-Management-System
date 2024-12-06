from django import forms
from .models import Book

# Form to handle book data
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields= ['title', 'authors', 'isbn', 'borrower', 'is_available', 'additional_info']

    
    # Custom validation for ISBN field
    def clean_isbn(self):  # Form validation
        isbn = self.cleaned_data.get('isbn')
        if len(isbn) != 13:
            raise forms.ValidationError('ISBN must be exactly 13 characters long.')
        return isbn