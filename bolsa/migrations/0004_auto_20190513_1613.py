# Generated by Django 2.2.1 on 2019-05-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0003_auto_20190513_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativos',
            name='codigo',
            field=models.CharField(max_length=5, unique=True, verbose_name='Código do Ativo'),
        ),
    ]
