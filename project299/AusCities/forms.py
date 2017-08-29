from django import forms
#Model form for use of databases elements in the form
class LoginForm(forms.Form):
    user = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
#class MenuForm(forms.Form):
    #about = forms.