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
