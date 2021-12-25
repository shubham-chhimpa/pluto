from django.contrib.auth.models import AbstractUser
from django.db import models

from AuthEngine.managers import PlutoUserManager


class PlutoUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PlutoUserManager()

    def __str__(self):
        return self.email
