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


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):  # Validate passwords
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


# UserProfile form for additional details
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['contact_number', 'address']