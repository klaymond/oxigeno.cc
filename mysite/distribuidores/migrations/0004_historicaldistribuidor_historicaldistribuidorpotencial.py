# Generated by Django 3.1.5 on 2021-03-22 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidores', '0003_auto_20210322_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDistribuidorPotencial',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('direccion', models.TextField()),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('horario', models.CharField(default='', max_length=100)),
                ('rfc', models.CharField(max_length=13)),
                ('ofrece_venta_de_tanque', models.BooleanField()),
                ('ofrece_renta_de_tanque', models.BooleanField()),
                ('ofrece_recarga_de_tanque', models.BooleanField()),
                ('ofrece_venta_de_concentrador', models.BooleanField()),
                ('ofrece_renta_de_concentrador', models.BooleanField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('estado_procedencia', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='distribuidores.estado')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical distribuidor potencial',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDistribuidor',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('horario', models.CharField(default='', max_length=100)),
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
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('estado_procedencia', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='distribuidores.estado')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical distribuidor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
