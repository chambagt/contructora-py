from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    dpi = models.CharField(max_length=15, unique=True)
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre