# Generated by Django 3.2.4 on 2021-06-02 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicians',
            name='musicians_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 3', regex='^.{3}$')]),
        ),
    ]
