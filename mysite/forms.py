from django import forms

from .models import currency

class currencyForm(forms.ModelForm):
      class Meta:
            model = currency
            fields = ['currency_from','currency_to','currency_input']

    
