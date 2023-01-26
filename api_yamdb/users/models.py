from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[validate_username]
    )
    confirmation_code = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    bio = models.TextField(
        blank=True,
    )
    USERS_ROLE_CHOICES = [
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    ]
    role = models.CharField(
        max_length=20,
        choices=USERS_ROLE_CHOICES,
        default='user',
    )
    email = models.EmailField(
        unique=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user')
        ]

    def __str__(self):
        return self.username

    @property
    def is_moder(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.is_superuser or self.role == "admin" or self.is_staff
