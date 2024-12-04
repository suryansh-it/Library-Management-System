from django.contrib import admin
from .models import Author
from .models import Book
from .models import Borrower
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name' , 'date_of_birth')  #display these columns
    search_fields =('first_name', 'last_name')  #search by these fields
    list_filter= ('date_of_birth',)  #filter by date of birth

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'authors' , 'idbn','borrower')  
    search_fields =('title', 'isbn')  
    list_filter= ('borrower',)

    # Custom method to display additional info in a readable format
    def get_additional_info(self,obj):
        return obj.additional_info.get('genre','N/A')
    get_additional_info.short_description = 'Genre'
    
        

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin)