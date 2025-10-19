from django.db import models
from django.urls import reverse

class Army(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    size = models.IntegerField()
    weapons = models.CharField(max_length=150)
    year = models.IntegerField()
    leader = models.CharField(max_length=150)
    details = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('army-detail', kwargs={'army_id': self.id})
