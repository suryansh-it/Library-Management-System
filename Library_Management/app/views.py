#Using DRF Viewsets for easy CRUD operations.
#Created Views (API Endpoints)

from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Author, Book, Borrower
from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserProfileForm

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request , *args, **kwargs):
        # Custom logic for assigning a borrower
        borrower_id = request.data.get('borrower')
        if borrower_id:
            try : 
                borrower =  Borrower.objects.get(id= borrower_id)
            
            except Borrower.DoesNotExist:
                return Response({'error': "Borrower does not exist"}, status= status.HTTP_400_BAD_REQUEST)
            

        return super().create(request, *args, **kwargs)


    def retrieve(self, request, *args, **kwargs):
        
        instance = self.get_object()
        data = self.get_serializer(instance).data
        data['message'] = 'Detailed information about the book'
        return Response(data)




class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


# Register view
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()


            login(request, user)  # Automatically log in user
            return redirect('dashboard')
        
    else :
        user_form =UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


        