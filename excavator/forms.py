from django import forms
from .models import Excavator


class ExcavatorForm(forms.ModelForm):

    class Meta:
        model = Excavator
        fields = '__all__'
