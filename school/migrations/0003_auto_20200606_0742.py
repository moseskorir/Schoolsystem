# Generated by Django 3.0.6 on 2020-06-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200606_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
