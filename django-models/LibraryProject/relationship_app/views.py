from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from .models import Book
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import BookForm 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
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

class LibraryDetailView(DetailView):
    pass

class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

# Role-checking functions
def is_admin(user):
    return UserProfile.objects.filter(user=user, role="Admin").exists()

def is_librarian(user):
    return UserProfile.objects.filter(user=user, role="Librarian").exists()

def is_member(user):
    return UserProfile.objects.filter(user=user, role="Member").exists()

# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Edit a book (Only users with "can_change_book" permission)
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Delete a book (Only users with "can_delete_book" permission)
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})