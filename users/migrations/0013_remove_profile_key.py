# Generated by Django 2.2.3 on 2019-11-13 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191111_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='key',
        ),
    ]
