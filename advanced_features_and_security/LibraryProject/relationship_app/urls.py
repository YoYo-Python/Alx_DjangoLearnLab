from django.urls import path
from django.contrib.auth import views as auth_views
from .views import book_view, LibraryBooksListView, RegistrationView, add_book, delete_book, edit_book
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Book-related views
    path('book/', book_view, name='book-list'),
    path('library/<int:pk>/books/', LibraryBooksListView.as_view(), name='library-books'),
    
    # Authentication views
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Password management
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Book management views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # ✅ FIXED: Added book_id
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  # ✅ FIXED: Added book_id
]
