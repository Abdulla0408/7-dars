from django import forms
from .models import ProductEnter

class ProductEnterForm(forms.ModelForm):
    class Meta:
        model = ProductEnter
        fields = '__all__'