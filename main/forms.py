# forms.py

from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['idusers'] 
        fields = ['firstname', 'lastname', 'age', 'email', 'password']
