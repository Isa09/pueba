from django.db import models


class estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    identificacion = models.IntegerField(primary_key=True)
    correo = models.EmailField(max_length=200, null=True, blank=True)
    p_academico = models.CharField(max_length=100)