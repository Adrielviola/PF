from django.db import models


class Carreras(models.Model):
    nombre = models.CharField(max_length=40)
    kilometros = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre
    
class Corredores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

