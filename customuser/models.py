from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class ExtendUser(AbstractUser):
    # adding unique related name
    groups = models.ManyToManyField(
        Group,
        related_name='extenduser_groups',
        blank=True,
        help_text='The Group s this user belongs to'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='extenduser_permissions',
        blank=True,
        help_text='Specific Permissions for this user'

    )
    email = models.EmailField(blank=False, max_length=100)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
