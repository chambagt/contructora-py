from django.db import models

class Maquinaria(models.Model):
    nombre = models.CharField(max_length=100)
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    precio_hora = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre