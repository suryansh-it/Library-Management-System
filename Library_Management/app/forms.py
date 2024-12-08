from django import forms
from .models import Book
from django.contrib.auth.models import User
from .models import UserProfile



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
    

# User registration form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
