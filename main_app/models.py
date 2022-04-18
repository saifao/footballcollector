from django.db import models
from django.forms import IntegerField
from django.urls import reverse
from django.db.models import Sum

POS = (('F', 'Forward'),('M', 'Midfielder'),('LB/RB', 'Left/Right Back'),('CB', 'Center Back'))

class Trophy(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        print(self)
        return reverse('trophies_detail', kwargs={'pk': self.id})


class Player(models.Model):
    name = models.CharField('Player Name', max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=10, choices=POS)
    mkt_value = models.IntegerField('Market Value')
    contract_exp = models.DateField('Contract Expiration')
    titles = models.ManyToManyField(Trophy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player', kwargs={'player_id': self.id})
    
    def income(self):
        return self.wage_set.all().aggregate(Sum('amount'))

class Wage(models.Model):
    amount = models.IntegerField('Salary Amount', default=0)
    payday = models.DateField('Date Paid')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.amount} paid on {self.payday}"
    
    class Meta:
        ordering = ['-payday']

