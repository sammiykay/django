# Generated by Django 3.1.2 on 2020-11-08 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='title',
        ),
    ]
