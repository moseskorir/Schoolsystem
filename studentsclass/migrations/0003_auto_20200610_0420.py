# Generated by Django 3.0.6 on 2020-06-10 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200606_0742'),
        ('studentsclass', '0002_auto_20200609_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='Student',
        ),
        migrations.AddField(
            model_name='subjects',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='term',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], max_length=1),
        ),
    ]
