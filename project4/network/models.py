from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    color = models.CharField(max_length=7)
    members = models.ManyToManyField(User, related_name='teams', default=None, null=True,)
    
    def save(self, *args, **kwargs):
        self.color = self.color.lower()
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects', default=None, null=True,)
    color = models.CharField(max_length=7, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.color = self.team.color.lower()
        super().save(*args, **kwargs)


class Task(models.Model):
    name = models.CharField(max_length=255)
    objective = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default=None, null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_to')

    def save(self, *args, **kwargs):
        self.color = self.project.color.lower()
        super().save(*args, **kwargs)