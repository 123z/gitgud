from django import forms
from django.forms import ModelForm

from .models import User
#Model form for use of databases elements in the form
class LoginForm(forms.Form):
    user = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
#class MenuForm(forms.Form):
    #about = forms.
class UserForm(ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'userType', 'email']
        widgets = { 'password': forms.PasswordInput, }
    def clean(self):
        cleanedData = super(UserForm, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        if password != confirm:
            raise forms.ValidationError("Password doesn't match")