# Create your models here.
# Create your models here.
from django.db import models

class Jogadores(models.Model):
    player_name = models.CharField(max_length=100, verbose_name="Nome do jogador")
    political_party = models.ForeignKey(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        
class Partido(models.Model):
    party_name = models.CharField(max_length=100, verbose_name="Nome do partidor")
    def __str__(self):
        return self.party_name
    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        
class Cenario(models.Model):
    scenario_description