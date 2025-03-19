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

-------------

# Retrieve Book Details


from .models import Book  # Import the Book model

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

-------------

# Update Book Title


from .models import Book  # Import the Book model

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

# Display confirmation
print(f"Updated Title: {book.title}")

--------------

# Delete Book Instance

from .models import Book  # Import the Book model

# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try retrieving all books to confirm deletion
books = Book.objects.all()
print("Remaining Books:", list(books))  # Should print an empty list if deletion was successful
