# Generated by Django 4.1 on 2022-09-01 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_remove_movimientos_hora_movimientos_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cuentas.cliente'),
            preserve_default=False,
        ),
    ]
