from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model with email as the unique identifier.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  # Ensuring default active status
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields["is_staff"] is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields["is_superuser"] is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user  # ✅ Corrected to ensure all fields are set explicitly
