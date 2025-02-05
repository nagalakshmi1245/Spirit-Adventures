from django import forms
from .models import *
from django.contrib.auth.models import User

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

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

    def save(self):
        obj=super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save()
        return obj
    
class signinform(forms.ModelForm):
    class Meta:
        model=signinModel
        fields=['username','password']
