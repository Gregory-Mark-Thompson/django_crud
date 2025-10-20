from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

OUTCOME = (
    ('W', 'Victory'),
    ('L', 'Defeat'),
    ('D', 'Draw')
)

class Army(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    size = models.IntegerField()
    weapons = models.CharField(max_length=150)
    year = models.IntegerField()
    leader = models.CharField(max_length=150)
    details = models.CharField(max_length=300)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('army-detail', kwargs={'army_id': self.id})

class Battle(models.Model):
    date = models.DateField('Final day of the battle or siege')
    location = models.CharField(max_length=150)
    enemy = models.CharField(max_length=150)
    losses = models.IntegerField()
    enemy_losses = models.IntegerField()
    outcome = models.CharField(max_length=1, choices=OUTCOME, default=OUTCOME[0][0])
    discussion = models.CharField(max_length=250)

    army = models.ForeignKey(Army, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_outcome_display()} at {self.location} on {self.date}"

    class Meta:
        ordering = ['-date']
