# Generated by Django 4.1.5 on 2023-02-02 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_remove_team_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_users',
            field=models.ManyToManyField(default=None, null=True, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='team_users',
            field=models.ManyToManyField(default=None, null=True, related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
    ]