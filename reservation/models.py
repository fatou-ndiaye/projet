from django.db import models

# Create your models here.
from django.db import models

class Trajet(models.Model):
    depart = models.CharField(max_length=30)
    arrivee = models.CharField(max_length=30)
    

    def __str__(self):
        return "%s %s" % (self.depart, self.arrivee)

class Vol(models.Model):
    prix= models.FloatField(max_length=100)
    date = models.CharField(max_length=20)
    heure = models.CharField(max_length=15)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    class Meta:
        ordering = ['id']

class Compagnie(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    vols = models.ManyToManyField(Vol)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nom        
