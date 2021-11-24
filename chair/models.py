from django.contrib.auth.models import User
from django.db import models


class ChairModel(models.Model):
    ubicacion = models.CharField(max_length=255, default='Estacion de carga')
    estado = models.CharField(max_length=255, default='Libre')
    destino = models.CharField(max_length=255, default='"En blanco"')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        if len(str(self.id)) == 1:
            id = 'PHX-00' + str(self.id)
        elif len(str(self.id)) == 2:
            id = 'PHX-0' + str(self.id)
        else:
            id = self.id
        return id
