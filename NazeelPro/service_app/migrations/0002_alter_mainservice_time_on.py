

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainservice',
            name='time_on',
            field=models.DateTimeField(),
        ),
    ]
