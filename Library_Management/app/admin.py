from django.contrib import admin
from .models import Author
from .models import Book
from .models import Borrower
from django.utils.html import format_html
# Register your models here.



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'display_authors' , 'isbn','borrower')  
    search_fields =('title', 'isbn')  
    list_filter= ('borrower',)

    # Custom method to display additional info in a readable format
    def get_additional_info(self,obj):
        return obj.additional_info.get('genre','N/A')
    get_additional_info.short_description = 'Genre'
    

        # Admin action to mark selected books as unavailable
    actions = ['mark_as_unavailable']

    def mark_as_unavailable(self,request, queryset):
        queryset.update(is_available= False)
        self.message_user(request, f'{queryset.count()} books marked as unavailable')
    mark_as_unavailable.short_description ='Mark selected books as  unavailable'


    # Custom method to display authors
    def display_authors(self, obj):
        # Aggregates all author names into a single string
        """
        Custom method to display a list of authors for each book.
        Django Admin doesn't allow many-to-many fields directly in list_display.
        """
        return ", ".join(author.first_name + " " + author.last_name for author in obj.authors.all())

    display_authors.short_description = 'Authors'  # Column label in admin 


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name' , 'date_of_birth')  #display these columns
    search_fields =('first_name', 'last_name')  #search by these fields
    list_filter= ('date_of_birth',)  #filter by date of birth



@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')



# Django Admin does not support displaying many-to-many fields directly in the list_display.
# The authors field in the Book model is a many-to-many relationship, so including it in list_display causes the issue.

# Solution:
# To include many-to-many fields in list_display, you can define a custom method inthe admin class 
# that aggregates the related data into a string format and then include that method in the list_display instead.