from django.db import models


# Custom Manager to filter available books
# class AvailableBookManager(models.Manager):  # Custom model manager
#     def get_queryset(self):
#         return super().get_queryset().filter(is_available=True)


class Author(models.Model):             # Many-to-Many relationship with Book
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Book(models.Model):                  # One-to-One: Borrower | Many-to-Many: Author
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')   # Many-to-Many relationship
    isbn = models.CharField(max_length=13)
    borrower = models.OneToOneField('Borrower', on_delete=models.SET_NULL, null=True, blank=True)   # One-to-One relationship
    #borror , on delete : deletes model when field is null
    additional_info = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title  #return title when the obj is printed
    
    is_available = models.BooleanField(default=True)     # Boolean to track availability


class Borrower(models.Model):           # One-to-Many with Book (via borrower field in Book)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'