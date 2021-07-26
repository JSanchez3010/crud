from django.db import models

class Usuario(models.Model):
    nombre= models.CharField(max_length=20)
    


    def __str__(self):
        return self.nombre








class Programador(models.Model):
    especialidad = models.CharField(max_length=30)
    empresa = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self): 
        return self.nombre
    