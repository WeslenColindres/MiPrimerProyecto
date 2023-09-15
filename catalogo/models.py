from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, 
on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
