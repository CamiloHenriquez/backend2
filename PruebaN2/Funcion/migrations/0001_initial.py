# Generated by Django 4.2.7 on 2023-11-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracionFuncion', models.CharField(max_length=20)),
                ('nombreFuncion', models.CharField(max_length=20)),
                ('horarioFuncion', models.CharField(max_length=30)),
                ('tipoFuncion', models.PositiveIntegerField()),
                ('generoFuncion', models.CharField(max_length=30)),
                ('restriccionEdad', models.CharField(choices=[('mayor de edad', '+18'), ('TE', 'Todo espectador'), ('mayor de 14', '14')], max_length=30)),
            ],
        ),
    ]