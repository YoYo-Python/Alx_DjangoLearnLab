from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Author, Book, Library, Librarian, UserProfile

# Register models that don’t require customization
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)

class CustomUserAdmin(UserAdmin):
    """Custom admin panel for managing CustomUser model."""
    
    model = CustomUser

    # Fields to be displayed in the admin panel
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_active')
    
    # Fields to filter by
    list_filter = ('is_staff', 'is_active')
    
    # Fieldsets for detailed view (editing users)
    fieldsets = (
        ('Personal Info', {'fields': ('email', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to show when creating a new user
    add_fieldsets = (
        ('Create User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)  # Sort by email instead of username

# Register the CustomUser model in Django Admin
admin.site.register(CustomUser, CustomUserAdmin)
