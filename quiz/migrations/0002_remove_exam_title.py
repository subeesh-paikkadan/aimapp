# Generated by Django 4.1.3 on 2022-11-29 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='title',
        ),
    ]
