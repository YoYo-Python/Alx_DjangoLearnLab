from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Library, Book, UserProfile
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import BookForm
from django.contrib.auth.decorators import permission_required

# List all books
def book_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Detail view for a library and its books
class LibraryBooksListView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.get_object().books.all()
        return context

# Library Detail View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# User Registration View
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

# Role-based views
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add a book
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # ✅ FIXED URL name
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Edit a book
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # ✅ FIXED URL name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# Delete a book
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')  # ✅ FIXED URL name
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})
