from django.db import models


class Frase(models.Model):
    contenido = models.CharField(max_length=255)

    def __str__(self):
        return self.contenido
