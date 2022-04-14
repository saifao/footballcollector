from django.forms import ModelForm
from .models import Wage

class WageForm(ModelForm):
    class Meta:
        model = Wage
        fields = ['amount', 'payday']