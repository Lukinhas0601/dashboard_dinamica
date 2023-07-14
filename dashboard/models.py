from django.db import models

# Create your models here.
class CentroEsportivos(models.Model):
    nome = models.CharField(max_length=100)
    data_entrada = models.DateField()
    