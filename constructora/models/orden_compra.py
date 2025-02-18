from django.db import models

class OrdenCompra(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden #{self.id} - {self.material.nombre_mat}"