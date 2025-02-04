from django import forms
from .models import *

class userInfoForm(forms.ModelForm):
    class Meta:
        model=userinfoModel
        fields='__all__'
        
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'