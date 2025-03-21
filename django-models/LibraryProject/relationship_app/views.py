from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from .models import Book
from django.views.generic import ListView
# Create your views here.
def book_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryBooksListView(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        library_id = self.kwargs.get("pk")  # Get library ID from URL
        return Library.objects.get(pk=library_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.get_queryset().books.all()  # Fetch books
        return context