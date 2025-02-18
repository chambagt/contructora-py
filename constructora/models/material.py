from django.db import models

class Material(models.Model):
    nombre_mat = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_mat