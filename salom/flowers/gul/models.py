from django.db import models

class Turlar(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Gullar(models.Model):
    nom = models.CharField(max_length=100)
    tavsif = models.TextField()
    turlar = models.ForeignKey(Turlar, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
