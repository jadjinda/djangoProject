from django.db import models

from compte.models import Compte


# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

class Transaction(models.Model):
    montant = models.DecimalField(max_digits=65,decimal_places=2)
    date = models.DateField()
    description = models.TextField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)

