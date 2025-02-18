from django.db import models

class ManoObra(models.Model):
    descripcion = models.CharField(max_length=100)
    unidad = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion