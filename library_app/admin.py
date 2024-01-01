from django.contrib import admin
from .models import Book , Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year', 'isbn','price']



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','address',]

