# Generated by Django 4.1.5 on 2023-02-01 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_project_team_task_project_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='users',
        ),
    ]
