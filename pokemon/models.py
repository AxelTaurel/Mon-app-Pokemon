from django.conf import settings
from django.db import models
from django.utils import timezone


class carte(models.Model):  # Modèle pour une carte Pokémon
    title = models.CharField(max_length=200)  # Nom de la carte
    description = models.TextField(default="Description par défaut")  # Ajout d'un défaut
    image_url = models.URLField(blank=False, null=False, default="data:image/png;base64,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")
    type = models.CharField(max_length=50, blank=True, null=True)  # Type de la carte (exemple : Plante, Feu)
    Pv = models.IntegerField(blank=False, null=False, default=0) 

    def __str__(self):
        return self.title


class Attaque(models.Model):  # Modèle pour une attaque associée à une carte
    carte = models.ForeignKey(carte, on_delete=models.CASCADE, related_name='attaques')  # Lien vers une carte
    name = models.CharField(max_length=100)  # Nom de l'attaque
    power = models.IntegerField()  # Puissance de l'attaque
    description = models.TextField(blank=True, null=True)  # Description ou détails de l'attaque

    def __str__(self):
        return self.name
