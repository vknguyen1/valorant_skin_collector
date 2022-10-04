from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


VARIANTS = (
    ('G', 'Green'),
    ('B', 'Blue'),
    ('R', 'Red'),
)

# Create your models here.

class Riot_Account(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})


class Skin(models.Model):
        name = models.CharField(max_length=100)
        weapon = models.CharField(max_length=100)
        price = models.IntegerField()
        riot_accounts = models.ManyToManyField(Riot_Account)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse('detail', kwargs={'skin_id': self.id})

class Skin_Variant(models.Model):
    date = models.DateField()
    variant = models.CharField(max_length=1, choices=VARIANTS, default=[0][0])
    skin = models.ForeignKey(Skin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_variant_display()} for {self.skin.name} on {self.date}'