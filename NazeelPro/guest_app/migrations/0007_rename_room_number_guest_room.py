# Generated by Django 4.1.7 on 2023-06-15 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_app', '0006_remove_guest_room_alter_guest_room_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='room_number',
            new_name='room',
        ),
    ]
