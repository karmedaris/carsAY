# Generated by Django 5.0.6 on 2024-12-13 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ci', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mo', models.CharField(max_length=100)),
                ('placa_mo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pro', models.CharField(max_length=100)),
                ('apellido_pro', models.CharField(max_length=100)),
                ('email_pro', models.EmailField(max_length=100)),
                ('telefono_pro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricacion_ve', models.IntegerField()),
                ('precio_ve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color_ve', models.CharField(max_length=100)),
                ('fk_id_ci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehiculos.ciudad')),
                ('fk_id_mo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehiculos.modelo')),
                ('fk_id_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehiculos.propietario')),
            ],
        ),
    ]
