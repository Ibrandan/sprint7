# Generated by Django 4.1 on 2022-08-29 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditoriacuenta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='direccion',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='direccioncliente',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='movimientos',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipocliente',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipocuenta',
            options={'managed': True},
        ),
    ]