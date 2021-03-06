# Generated by Django 3.0.6 on 2020-06-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Report_Card',
            new_name='ReportCard',
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='student',
            name='registration_number',
        ),
        migrations.AddField(
            model_name='student',
            name='registration_number',
            field=models.CharField(max_length=50, unique=True, verbose_name='RegNumber'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
