import os
import django
import sys

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Initialize Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
library = Library.objects.first()

# Author.objects.get(name=author_name)", "objects.filter(author=author)
def query_books_by_author(author_name):
    """ Query all books written by a specific author. """
    books = Book.objects.filter(author_name=author_name)
    return books

def list_all_books_in_library(library_name):
    """ List all books available in a specific library. """
    books = Library.books.all()
    return books

def get_librarian_for_library(library_name):
    """ Retrieve the librarian for a specific library. """
    try:
        library = Librarian.objects.get(library=library_name)
        return library # Assuming a OneToOneField to Librarian
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
