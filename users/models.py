from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    # username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    other_name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
    