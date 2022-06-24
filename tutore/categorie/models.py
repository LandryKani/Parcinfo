from django.db import models

# Create your models here.


class Categorie(models.Model):
    codec = models.CharField(max_length=20, null=False)
    nomc = models.CharField(max_length=200, null=False)
    quantite = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.codec + ' : ' + self.nomc