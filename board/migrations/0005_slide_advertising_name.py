# Generated by Django 2.2.3 on 2019-07-30 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20190730_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide_advertising',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
