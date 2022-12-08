from django.db import models

class Deudor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    version = models.FloatField()
    creditscore = models.FloatField(default=None, null=True)

    def __str__(self):
        return self.nombre


# Create your models here.
