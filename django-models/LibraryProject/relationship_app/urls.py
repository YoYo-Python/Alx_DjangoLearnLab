from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from .views import book_view, LibraryBooksListView, RegistrationView, add_book,delete_book,edit_book
# from .views import list_books, LibraryDetailView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# views.register
urlpatterns = [
    path('book/', book_view, name='book-list'),
    path("library/<int:pk>/books/", LibraryBooksListView.as_view(), name="library-books"),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', edit_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),

]
