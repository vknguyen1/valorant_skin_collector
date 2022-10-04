from django.contrib import admin

# Register your models here.
from .models import Skin, Skin_Variant, Riot_Account


# from. models import Skin

admin.site.register(Skin)
admin.site.register(Skin_Variant)
admin.site.register(Riot_Account)
