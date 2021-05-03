from django import forms
from .models import DeditCard

class DeditCardCreateForm(forms.ModelForm):
    class Meta:
        model = DeditCard
        fields = ['number', 'expiry_month', 'expiry_year', 'cvv',
                  'pin']