from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author", "publication_year")
    # Enable search by title and author
    search_fields = ('title', 'author')  

    # Add filters for publication year
    list_filter = ('publication_year',) 

admin.site.register(Book,BookAdmin)