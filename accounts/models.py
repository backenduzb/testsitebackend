from django.contrib.auth.models import AbstractUser, BaseUserManager
from string import digits
from django.db import models
from random import choices

def generate_username(full_name: str):
    user_name = f"{full_name.replace(" ","").lower()}"
    return f"{user_name}{''.join(choices(digits, k=3))}"

class Class(models.Model):
    name = models.CharField(max_length=5)
    teacher_full_name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Foydalanuvchi nomi kiritilishi shart")
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_teacher', False)
        extra_fields.setdefault('is_student', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser uchun is_staff=True bo‘lishi kerak')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser uchun is_superuser=True bo‘lishi kerak')

        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    full_name = models.CharField(max_length=512, verbose_name="To'liq ism")
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name="Sinfi",
        null=True,
        blank=True
    )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.is_superuser:
            if not self.username:
                raise ValueError("Superuser uchun username kiritilishi shart")
            super().save(*args, **kwargs)
            return
        
        if not self.username and self.full_name:
            self.username = generate_username(self.full_name)

        self.save_base()
    
    def __str__(self):
        return f"{self.full_name}"