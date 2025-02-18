from django.db import models

class Rol(models.Model):
    rol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.rol