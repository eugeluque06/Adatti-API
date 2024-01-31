# Generated by Django 5.0.1 on 2024-01-21 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdattiAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('icono', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='alimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=100)),
                ('RPNA', models.IntegerField()),
                ('codigo_barras', models.IntegerField()),
                ('tipo_alimento', models.CharField(max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdattiAPI.categoria')),
                ('ingredientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdattiAPI.ingredientes')),
            ],
        ),
    ]