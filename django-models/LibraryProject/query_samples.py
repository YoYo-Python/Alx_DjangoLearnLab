import os
import django

# Set the environment variable for Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Initialize Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """ Query all books written by a specific author. """
    books = Book.objects.filter(author__name=author_name)
    return books

def list_all_books_in_library(library_name):
    """ List all books available in a specific library. """
    books = Book.objects.filter(library__name=library_name)
    return books

def get_librarian_for_library(library_name):
    """ Retrieve the librarian for a specific library. """
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Assuming a OneToOneField to Librarian
    except Library.DoesNotExist:
        return None

if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    # Query books by author
    books_by_author = query_books_by_author(author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # List books in library
    books_in_library = list_all_books_in_library(library_name)
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Get librarian for the library
    librarian = get_librarian_for_library(library_name)
    print(f"Librarian of {library_name}: {librarian.name if librarian else 'Not found'}")
