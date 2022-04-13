from django.db import models

POS = (('F', 'Forward'),('M', 'Midfielder'),('LB/RB', 'Left/Right Back'),('CB', 'Center Back'))

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=10, choices=POS)
    mkt_value = models.IntegerField()
    contract_exp = models.DateField()

    def __str__(self):
        return self.name

