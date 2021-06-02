# Generated by Django 3.2.4 on 2021-06-02 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20210602_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalbums',
            name='album_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 5', regex='^.{5}$')]),
        ),
    ]
