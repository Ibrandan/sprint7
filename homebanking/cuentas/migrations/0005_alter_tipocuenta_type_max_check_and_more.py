# Generated by Django 4.1 on 2022-08-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_alter_tipocuenta_type_max_check_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocuenta',
            name='type_max_check',
            field=models.IntegerField(verbose_name='Chequeras maximas'),
        ),
        migrations.AlterField(
            model_name='tipocuenta',
            name='type_max_deposit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Depositos maximos sin previo aviso'),
        ),
    ]
