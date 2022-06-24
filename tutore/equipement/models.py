from django.db import models

# Create your models here.
from categorie.models import Categorie


class Equipement(models.Model):
    code = models.CharField(max_length=200, null=False)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=False, default='equipement0')
    Etat = (('fontionnel', 'foncionnel'), ('en panne', 'en panne'))
    etat = models.CharField(max_length=200, null=False, default='fontionnel', choices=Etat)
    dateentrer = models.DateTimeField(null=True, auto_now_add=True)
    datemodif = models.DateTimeField(null=True, auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.code + ' : ' + self.nom + ' ... ' + self.etat + ' ... '