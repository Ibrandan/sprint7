# Generated by Django 4.1 on 2022-08-29 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaCuenta',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('old_id', models.IntegerField(blank=True, null=True)),
                ('new_id', models.IntegerField(blank=True, null=True)),
                ('old_balance', models.IntegerField(blank=True, null=True)),
                ('new_balance', models.IntegerField(blank=True, null=True)),
                ('old_iban', models.TextField(blank=True, null=True)),
                ('new_iban', models.TextField(blank=True, null=True)),
                ('old_type', models.IntegerField(blank=True, null=True)),
                ('new_type', models.IntegerField(blank=True, null=True)),
                ('user_action', models.TextField(blank=True, null=True)),
                ('created_at', models.TextField()),
            ],
            options={
                'db_table': 'auditoria_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_street', models.TextField()),
                ('address_street_number', models.TextField()),
                ('address_city', models.TextField()),
                ('address_country', models.TextField()),
            ],
            options={
                'db_table': 'Direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DireccionCliente',
            fields=[
                ('address_client_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('address_type_client', models.TextField()),
            ],
            options={
                'db_table': 'Direccion_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movement_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('operation_type', models.TextField(blank=True, null=True)),
                ('hora', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('client_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('type_client', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('type_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('type_account', models.TextField()),
            ],
            options={
                'db_table': 'tipo_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI', unique=True)),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
                ('customer_username', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
    ]
