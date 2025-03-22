from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author", "publication_year")
    # Enable search by title and author
    search_fields = ('title', 'author')  

    # Add filters for publication year
    list_filter = ('publication_year',) 

admin.site.register(Book,BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "name", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )
    search_fields = ("email", "name")
    ordering = ("email",)
    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)
