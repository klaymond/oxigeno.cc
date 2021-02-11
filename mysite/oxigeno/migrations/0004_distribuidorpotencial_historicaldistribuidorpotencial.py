# Generated by Django 3.1.5 on 2021-02-11 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oxigeno', '0003_auto_20210207_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistribuidorPotencial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_distribuidor', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.TextField()),
                ('horario', models.CharField(max_length=100)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('ofrece_venta_de_tanque', models.BooleanField()),
                ('ofrece_renta_de_tanque', models.BooleanField()),
                ('ofrece_recarga_de_tanque', models.BooleanField()),
                ('ofrece_venta_de_concentrador', models.BooleanField()),
                ('ofrece_renta_de_concentrador', models.BooleanField()),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'distribuidores potenciales',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDistribuidorPotencial',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('nombre_distribuidor', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.TextField()),
                ('horario', models.CharField(max_length=100)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('ofrece_venta_de_tanque', models.BooleanField()),
                ('ofrece_renta_de_tanque', models.BooleanField()),
                ('ofrece_recarga_de_tanque', models.BooleanField()),
                ('ofrece_venta_de_concentrador', models.BooleanField()),
                ('ofrece_renta_de_concentrador', models.BooleanField()),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical distribuidor potencial',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]