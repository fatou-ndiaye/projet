from django.core import validators
from django import forms
from reservation.models import Compagnie

class CompagnieRegistration(forms.ModelForm):
    class Meta:
        model=Compagnie
        fields=['nom','logo']