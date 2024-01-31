# Generated by Django 5.0.1 on 2024-01-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdattiAPI', '0002_categoria_ingredientes_alimentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='ingredientes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='RPNA',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='codigo_barras',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='ingredientes',
        ),
    ]
