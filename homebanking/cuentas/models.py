from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_username = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True,blank=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  
    customer_dni = models.TextField(db_column='customer_DNI', unique=True) 
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cliente'
    def __str__(self):
        nombre = self.customer_name + " " + self.customer_surname
        return nombre



class Movimientos(models.Model):
    movement_id = models.AutoField(primary_key=True, blank=True)
    account_number = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    operation_type = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movimientos'

class TipoCliente(models.Model):
    client_id = models.TextField(primary_key=True, blank=True)  
    type_client = models.TextField()

    class Meta:
        managed = True
        db_table = 'tipo_cliente'

class TipoCuenta(models.Model):
    type_id = models.AutoField(primary_key=True)  
    type_name = models.TextField(null=False)
    type_savings_usd = models.BooleanField('Caja de ahorro en dolares',null=False)
    type_max_with = models.IntegerField('Retiro diario maximo',null=False)
    type_commissions = models.FloatField('Porcentaje de comision (%)')
    type_max_cc = models.IntegerField('Tarjetas de credito maximas',null=False)
    type_max_dc = models.IntegerField('Tarjetas de debito maximas',null=False)
    type_max_check = models.IntegerField('Chequeras maximas')
    type_max_deposit = models.IntegerField('Depositos maximos sin previo aviso',blank=True,null=True)
    type_overdraft = models.FloatField('Descubierto',null=False)
    type_prestamos = models.FloatField('Prestamos pre aprobados')


    class Meta:
        managed = True
        db_table = 'tipo_cuenta'
    def __str__(self):
        return self.type_name

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='account_type', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'

class AuditoriaCuenta(models.Model):
    audit_id = models.AutoField(primary_key=True, blank=True)
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.IntegerField(blank=True, null=True)
    new_type = models.IntegerField(blank=True, null=True)
    user_action = models.TextField(blank=True, null=True)
    created_at = models.TextField()

    class Meta:
        managed = True
        db_table = 'auditoria_cuenta'

class DireccionCliente(models.Model):
    address_client_id = models.TextField(primary_key=True, blank=True) 
    address_type_client = models.TextField()

    class Meta:
        managed = True
        db_table = 'Direccion_cliente'

class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True, blank=True)
    address_street = models.TextField()
    address_street_number = models.TextField()
    address_city = models.TextField()
    address_country = models.TextField()
    address_type_required = models.ForeignKey('DireccionCliente', models.DO_NOTHING, db_column='address_type_required', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Direccion'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'

