from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name='activation code')

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.get_full_name()
