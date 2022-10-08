from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
