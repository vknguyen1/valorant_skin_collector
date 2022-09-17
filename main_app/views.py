from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

"""
Mock Database for Valorant Skins
"""

class Skin:
    def __init__(self, weapon, name, price):
        self.weapon = weapon
        self.name = name
        self.price = price

skins = [
    Skin('vandal', 'reaver', 1775),
    Skin('sheriff', 'reaver', 1775),
    Skin('phantom', 'ion', 1775),
    Skin('operator', 'magepunk', 2600)
]
def skins_index(request):
    return render(request, 'skins/index.html', {'skins': skins})