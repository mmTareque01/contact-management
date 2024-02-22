import uuid
from django.db import models
from django.utils import timezone


class User(models.Model):
    userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    userName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)


    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.updatedAt = timezone.now()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.isDeleted = True
        self.save()

    def __str__(self):
        return f"{self.userName} ({self.email})"


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
# from django.db import models
# from django.utils import timezone
# import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ['userName']

    def save(self, update_fields=None, *args, **kwargs):
        if update_fields is not None and 'password' in update_fields:
            # Remove 'password' from update_fields if present
            update_fields.remove('password')
        self.updatedAt = timezone.now()
        super().save(update_fields=update_fields, *args, **kwargs)

    def delete(self, *args, **kwargs):
        self.isDeleted = True
        self.save()

    def __str__(self):
        return f"({self.email})"
