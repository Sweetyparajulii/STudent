# Generated by Django 4.2.3 on 2023-07-04 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_sessionyear'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SessionYear',
            new_name='Session_years',
        ),
    ]
