# Generated by Django 2.2.1 on 2019-05-16 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa', '0007_compraativos_qtd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativos',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='ativos',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user_code_ativo', to='bolsa.FakeUser'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CompraAtivos',
        ),
    ]