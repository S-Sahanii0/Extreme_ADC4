from django import forms
from endUser.models import Seller

class LoginFormS(forms.ModelForm):
    class Meta:
         model=Seller
         fields=('username','password')