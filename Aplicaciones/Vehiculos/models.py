from django.db import models

class Propietario(models.Model):
    nombre_pro = models.CharField(max_length=100)
    apellido_pro = models.CharField(max_length=100)
    email_pro = models.EmailField(max_length=100)
    telefono_pro = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.nombre_pro} {self.apellido_pro}'

class Ciudad(models.Model):
    nombre_ci = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre_ci

class Modelo(models.Model):
    nombre_mo = models.CharField(max_length=100)
    placa_mo = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.nombre_mo} ({self.placa_mo})'

class Vehiculo(models.Model):
    fabricacion_ve = models.IntegerField()
    precio_ve = models.DecimalField(max_digits=10, decimal_places=2)
    color_ve = models.CharField(max_length=100)
    fk_id_pro = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    fk_id_ci = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fk_id_mo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def _str_(self):
        return f'{self.color_ve} - {self.fk_id_mo.nombre_mo} ({self.fk_id_mo.placa_mo})'