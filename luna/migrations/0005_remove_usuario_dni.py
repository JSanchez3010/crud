# Generated by Django 3.2.5 on 2021-07-22 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luna', '0004_programador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dni',
        ),
    ]
