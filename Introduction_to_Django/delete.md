# Delete Book Instance

from .models import Book  # Import the Book model

# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try retrieving all books to confirm deletion
books = Book.objects.all()
print("Remaining Books:", list(books))  # Should print an empty list if deletion was successful
