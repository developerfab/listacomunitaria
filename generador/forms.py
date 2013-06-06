from django import forms
from models import Lista, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=("username","password","email",)
        
class IngresoForm(forms.ModelForm):
    class Meta:
        model = User
        fields=("username","password",)
