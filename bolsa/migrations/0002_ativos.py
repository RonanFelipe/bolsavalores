# Generated by Django 2.2.1 on 2019-05-12 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ativos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Ação')),
                ('codigo', models.CharField(max_length=5, verbose_name='Código do Ativo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição do Ativo')),
            ],
        ),
    ]
