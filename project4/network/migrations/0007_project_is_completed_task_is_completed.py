# Generated by Django 4.1.5 on 2023-02-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_task_assigned_to_task_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
