import logging
from django import forms
from django.forms import ModelForm

from .models import User, User2
#Model form for use of databases elements in the form
class LoginForm(forms.Form):
    user = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class LoginModel(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your password...'}),
                    'username': forms.TextInput(attrs={'placeholder':'Enter your username...'}),
            }
    def clean(self):
        cleanedData = super(LoginModel, self).clean()
        cUsername = cleanedData.get("username")
        cPassword = cleanedData.get("password")
        try:
            User.objects.get(username__exact=cUsername, password__exact=cPassword)
        except User.DoesNotExist:
            raise forms.ValidationError("Username or password incorrect")
            
    
#class MenuForm(forms.Form):
    #about = forms.
class RegisterForm(ModelForm):
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password...'}))
    class Meta:
        model = User
        fields = ['username', 'password', 'userType', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Choose a password...'}),
                    'username': forms.TextInput(attrs={'placeholder':'Choose a username...'}),
                'email': forms.TextInput(attrs={'placeholder':'Enter a valid e-mail....'})
            }
    def clean(self):
        cleanedData = super(RegisterForm, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        logging.debug("Cleaned")
        if password != confirm:
            raise forms.ValidationError("Password doesn't match")
        
        if User.objects.filter(username__exact=cleanedData.get("username")).exists():
            raise forms.ValidationError("Username taken")
    
class RegisterForm2(ModelForm):
    class Meta:
        model = User2
        fields = ['username', 'password', 'usertype', 'email']
        widgets = { 'usertype' : forms.Select,}