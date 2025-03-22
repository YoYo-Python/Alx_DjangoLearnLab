from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser,PermissionsMixin

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUserManager(BaseUserManager):
    def create(self,email,password,**extra_fields):
        if not email:
            raise ValueError("You have not provided a valid email address!!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create(email,password,**extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create(email,password,**extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True,default='',unique=True)
    name = models.CharField(max_length=255, blank=True,default='')
    date_of_birth = models.DateField(null=True, blank=True)  
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)  
    # is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    objects = CustomUserManger()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

