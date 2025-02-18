from django.db import models

class Cliente(models.Model):
    nombre_representante = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    mail = models.EmailField(unique=True)

    def __str__(self):
        return self.empresa