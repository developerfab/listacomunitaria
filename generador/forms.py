from django import forms
from models import Lista, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
