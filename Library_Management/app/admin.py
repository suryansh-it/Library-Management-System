from django.contrib import admin
from .models import Author
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name' , 'date_of_birth')  #display these columns
    search_fields =('first_name', 'last_name')  #search by these fields
    list_filter= ('date_of_birth',)  #filter by date of birth

