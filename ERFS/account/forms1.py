from django import forms
from endUser.models import Seller

class RegistrationFormS(forms.ModelForm):
    class Meta:
         model=Seller
         fields=('seller_Name','seller_Contact','seller_Address')