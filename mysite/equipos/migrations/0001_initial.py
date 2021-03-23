# Generated by Django 3.1.5 on 2021-03-22 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distribuidores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofrece_renta', models.BooleanField(default=True)),
                ('disponibilidad_renta', models.IntegerField()),
                ('ofrece_venta', models.BooleanField(default=True)),
                ('disponibilidad_venta', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ofrece_recarga', models.BooleanField(default=True)),
                ('disponibilidad_recarga', models.IntegerField()),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidores.distribuidor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Concentrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofrece_renta', models.BooleanField(default=True)),
                ('disponibilidad_renta', models.IntegerField()),
                ('ofrece_venta', models.BooleanField(default=True)),
                ('disponibilidad_venta', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidores.distribuidor')),
            ],
            options={
                'verbose_name_plural': 'concentradores',
            },
        ),
    ]