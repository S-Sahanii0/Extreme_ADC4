from django import forms
from endUser.models import Buyer

class RegistrationFormB(forms.ModelForm):
    class Meta:
        model= Buyer
        fields=('buyer_Name','buyer_Contact','buyer_Address')

       

       
