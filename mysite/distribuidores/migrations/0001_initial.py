# Generated by Django 3.1.5 on 2021-03-22 04:31

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='DistribuidorPotencial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('direccion', models.TextField()),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('rfc', models.CharField(max_length=13)),
                ('horario', models.CharField(max_length=100)),
                ('ofrece_venta_de_tanque', models.BooleanField()),
                ('ofrece_renta_de_tanque', models.BooleanField()),
                ('ofrece_recarga_de_tanque', models.BooleanField()),
                ('ofrece_venta_de_concentrador', models.BooleanField()),
                ('ofrece_renta_de_concentrador', models.BooleanField()),
                ('estado_procedencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='distribuidores.estado')),
            ],
            options={
                'verbose_name_plural': 'distribuidores potenciales',
            },
        ),
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('estado', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('ciudad', models.CharField(max_length=100)),
                ('address', django_google_maps.fields.AddressField(default='', max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(default='', max_length=100)),
                ('dar_de_baja', models.BooleanField(default=False)),
                ('abre_sabado', models.BooleanField(default=True)),
                ('abre_domingo', models.BooleanField(default=True)),
                ('abre_24h', models.BooleanField(default=True)),
                ('recarga_gratis', models.BooleanField(default=False)),
                ('estado_procedencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='distribuidores.estado')),
            ],
            options={
                'verbose_name_plural': 'distribuidores',
            },
        ),
    ]
