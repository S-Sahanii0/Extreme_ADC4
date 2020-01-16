from django import forms
from endUser.models import Seller

class RegistrationFormS(forms.ModelForm):
    class Meta:
         model=Seller
         fields=('username','seller_Name','seller_Contact','seller_Address','password','confirm_password')