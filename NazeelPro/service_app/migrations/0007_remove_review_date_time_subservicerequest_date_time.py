# Generated by Django 4.1.7 on 2023-06-21 07:59

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0006_alter_review_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date_time',
        ),
        migrations.AddField(
            model_name='subservicerequest',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now()),
            preserve_default=False,
        ),
    ]
