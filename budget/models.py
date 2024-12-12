from django.db import models
from revenue.models import Categorie


# Create your models here.
class Budget(models.Model):
    montantMax = models.DecimalField(max_digits=65,decimal_places=2)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
