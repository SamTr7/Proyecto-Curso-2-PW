from django.db import models

# Estructura para un carro
class Carro(models.Model):
    marca = models.CharField(max_length=100) 
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.FloatField()  
    imagen = models.FileField(upload_to="carros/") 

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
