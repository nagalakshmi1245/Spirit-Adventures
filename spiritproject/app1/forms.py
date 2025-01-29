from django import forms
from .models import *
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'
