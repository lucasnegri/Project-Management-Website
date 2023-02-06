# Generated by Django 4.1.5 on 2023-02-04 03:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_rename_project_users_project_members_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]