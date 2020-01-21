from django import forms
from endUser.models import EndUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= EndUser
        fields=('username','Name','Contact','Address','password','confirm_password')

       

       
