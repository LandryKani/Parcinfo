from django.db import models

# Create your models here.


class Panne(models.Model):
    codep = models.CharField(max_length=20, null=False)
    nomp = models.CharField(max_length=200, null=False)
    priorite = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.codep + ' : ' + self.nomp