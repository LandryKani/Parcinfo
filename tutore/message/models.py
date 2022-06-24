from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=2400, null=True, default=' ')
    expediteur = models.CharField(max_length=40, null=True, default=' Anonymous ')
    destinataire = models.CharField(max_length=40, null=False)
    statut = models.CharField(max_length=15, null=True, default='unread')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expediteur + " " + self.statut + " : " + self.text