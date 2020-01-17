from django import forms
from endUser.models import Buyer

class LoginFormB(forms.ModelForm):
    class Meta:
        model= Buyer
        fields=('username','password')