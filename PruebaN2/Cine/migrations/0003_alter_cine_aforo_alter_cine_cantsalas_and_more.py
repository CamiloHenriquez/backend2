# Generated by Django 4.2.7 on 2023-11-19 22:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cine', '0002_alter_cine_aforo_alter_cine_cantsalas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cine',
            name='aforo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000000)]),
        ),
        migrations.AlterField(
            model_name='cine',
            name='cantSalas',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000000)]),
        ),
        migrations.AlterField(
            model_name='cine',
            name='telefono',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(911111111)]),
        ),
    ]
