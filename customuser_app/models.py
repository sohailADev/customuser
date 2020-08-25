from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUserModel(AbstractUser):
    displayname = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    homepage = models.URLField(null=True)
    REQUIRED_FIELDS = ['age']
    def __str__(self):
        return self.username
