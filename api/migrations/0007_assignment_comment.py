# Generated by Django 4.0.2 on 2022-04-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_assignment_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='comment',
            field=models.ManyToManyField(to='api.Comment'),
        ),
    ]
