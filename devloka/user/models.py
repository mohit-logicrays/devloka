from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User Model"""

    email = models.EmailField(verbose_name=_("Email"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    def __str__(self):
        return self.email
