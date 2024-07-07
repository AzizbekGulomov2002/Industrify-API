from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, email, name, password=None):
        if not phone:
            raise ValueError('Users must have a phone number')
        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, name, password):
        user = self.create_user(
            phone=phone,
            email=email,
            name=name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = None  # Remove username field
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone