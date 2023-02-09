# Generated by Django 4.1.5 on 2023-02-09 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_project_is_completed_task_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_teams', to=settings.AUTH_USER_MODEL),
        ),
    ]