# Generated by Django 2.2.3 on 2019-11-13 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0029_auto_20191113_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='update_dt',
        ),
    ]