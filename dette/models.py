from django.db import models

# Create your models here.
class Dette(models.Model):
    nom = models.CharField(max_length=100)
    montantTotal = models.DecimalField(max_digits=65,decimal_places=2)
    montantRestant = models.DecimalField(max_digits=65,decimal_places=2)
    dateEcheance = models.DateField()


