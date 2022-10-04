from django.forms import ModelForm
from .models import Skin_Variant

class VariantForm(ModelForm):
    class Meta:
        model = Skin_Variant
        fields = ('date', 'variant')