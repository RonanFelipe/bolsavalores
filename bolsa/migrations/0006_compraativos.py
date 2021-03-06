# Generated by Django 2.2.1 on 2019-05-13 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0005_fakeuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraAtivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ativo_code', to='bolsa.Ativos', verbose_name='Ativos Comprados')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_code', to='bolsa.FakeUser', verbose_name='Fake user')),
            ],
        ),
    ]
