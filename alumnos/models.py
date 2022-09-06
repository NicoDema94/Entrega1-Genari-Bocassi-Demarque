from django.db import models

class Alumnos(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)


class Ubicacion(models.Model):
    provincia = models.CharField(max_length=128)
    barrio = models.CharField(max_length=128)


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    comision = models.IntegerField()