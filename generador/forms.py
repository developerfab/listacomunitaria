from django import forms
from models import Lista

class UserForm(forms.ModelForm):
    class Meta:
        model = User
