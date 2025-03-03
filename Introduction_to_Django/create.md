# Create a Book Instance

from .models import Book  # Import the Book model

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Print confirmation

print("Book created successfully:", book)

