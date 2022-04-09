# Generated by Django 4.0.2 on 2022-04-09 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_assignment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='user',
        ),
        migrations.AddField(
            model_name='assignment',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
