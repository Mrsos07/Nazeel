# Generated by Django 4.1.7 on 2023-06-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0009_guest_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
