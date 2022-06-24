from django.db import models

# Create your models here.
from equipement.models import Equipement
from panne.models import Panne


class Statut(models.Model):
    # il s'agit de l'etat de la panne
    equipement = models.ForeignKey(Equipement, null=True, on_delete=models.CASCADE)
    panne = models.ForeignKey(Panne, null=True, on_delete=models.CASCADE)
    EtatP = (('Non Resolu', 'Non Resolu'), ('Resolu', 'Resolu'))
    etatp = models.CharField(max_length=200, null=False, default='Non Resolu', choices=EtatP)
    # etatp = etat de la panne
    datesg = models.DateField(null=True, auto_now_add=True)

    # datesg = date signalement

    def __str__(self):
        return self.equipement.nom + ' ... Etat panne: ' + self.etatp + ' ... '