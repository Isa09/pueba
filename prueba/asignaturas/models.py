from django.db import models
from estudiante.models import estudiante

class asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    salon = models.CharField(max_length=10)
    horario = models.CharField(max_length=200)
    id_profesor = models.IntegerField()

class clase(models.Model):
    id_estudiante = models.ForeignKey(estudiante, on_delete=models.CASCADE)
    id_signatura = models.ForeignKey(asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_signatura.nombre)
