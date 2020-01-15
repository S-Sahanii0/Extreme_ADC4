from django import forms
from endUser.models import Buyer,Seller

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Buyer
        fields=('buyer_Name','buyer_Contact','buyer_Address')

       # model= Seller
       # fields=('seller_Name','seller_contact','seller_Address')

       
