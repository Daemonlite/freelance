# Generated by Django 4.0.4 on 2022-07-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0003_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='CVC',
            field=models.BigIntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Card_Number',
            field=models.BigIntegerField(max_length=16),
        ),
    ]
