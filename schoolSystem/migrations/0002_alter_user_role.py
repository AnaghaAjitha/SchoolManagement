# Generated by Django 4.2.13 on 2024-07-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=20, null=True),
        ),
    ]
