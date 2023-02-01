from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField()
    color = models.CharField(max_length=50)
    selected_users = models.ManyToManyField(User, related_name='teams')
