from django.urls import path
from .views import book_view, LibraryBooksListView

urlpatterns = [
    path('book/', book_view, name='book-list'),
    path("library/<int:pk>/books/", LibraryBooksListView.as_view(), name="library-books"),

]
