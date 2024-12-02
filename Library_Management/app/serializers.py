#Serializers convert models into JSON format and validate input data.
from rest_framework import serializers
from .models import Author, Book, Borrower

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields= '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many= True , read_only =True)
    author_ids = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all() , many = True , read_only = True, source ='authors'
    )

    class Meta:
        model = Book
        fields =['id' , 'title' , 'authors' , 'author_ids' ,   'isbn' ,'borrower' ,'additional_info']


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'