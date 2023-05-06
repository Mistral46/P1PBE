from django.db import models

class Lada(models.Model):
   Anno = models.DateField(max_length = 255)
   Marca = models.TextField(max_length = 255)
   Color = models.TextField(max_length = 255)
   Combustible = models.TextField(max_length = 255)
   NumPuertas = models.TextField(max_length = 255)
   Traccion = models.TextField(max_length = 255)
