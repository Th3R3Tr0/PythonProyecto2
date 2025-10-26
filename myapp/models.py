from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()


    def __str__(self):
        return self.nombre


class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()


    def __str__(self):
        return self.nombre
    
class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # encripta la contraseña antes de guardar
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"