# Generated by Django 2.2.1 on 2019-05-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0004_auto_20190513_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do usuário')),
                ('nacionalidade', models.CharField(max_length=255, verbose_name='País de Origem')),
            ],
        ),
    ]