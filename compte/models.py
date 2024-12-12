from django.db import models

# Create your models here.
class Compte(models.Model):
    nom = models.CharField(max_length=50)
    solde = models.DecimalField(max_digits=10, decimal_places=2)
    #devise = models.