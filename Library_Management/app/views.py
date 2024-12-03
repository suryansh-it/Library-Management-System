#Using DRF Viewsets for easy CRUD operations.
#Created Views (API Endpoints)

from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book, Borrower
from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer
from rest_framework.response import Response
from rest_framework import status 

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


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer