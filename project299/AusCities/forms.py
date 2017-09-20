import logging
from django import forms
from django.forms import ModelForm
from django.contrib.auth import hashers


from .models import User
#Model form for use of databases elements in the form
    
class LoginModel(ModelForm):
    class Meta:
        model = User
        fields = ['emailaddress', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your password...'}),
                    'emailaddress': forms.TextInput(attrs={'placeholder':'Enter your username...'}),
            }
        labels = {
                'emailaddress': 'E-mail address',
            }
    def clean(self):
        cleanedData = super(LoginModel, self).clean()
        cUsername = cleanedData.get("emailaddress")
        try:
            user = User.objects.get(emailaddress__iexact=cUsername)
            if hashers.check_password(cleanedData.get("password"), user.password):
                logging.debug(user.usertype)
            else:
                raise forms.ValidationError("Username or password incorrect")
        except User.DoesNotExist:
            raise forms.ValidationError("Username or password incorrect")
            
class RegisterForm(ModelForm):
    confirm = forms.CharField(label ='Confirm password',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password...'}))
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Choose a password...'}),
                    'firstname': forms.TextInput(attrs={'placeholder':'Enter your given name...'}),
                'lastname': forms.TextInput(attrs={'placeholder':'Enter your surname...'}),
                'emailaddress': forms.EmailInput(attrs={'placeholder':'Enter a valid e-mail....'})
            }
        labels = {
                'emailaddress': 'E-mail address',
                'firstname': 'First name',
                'lastname': 'Last name',
                'usertype': 'User type',
            }
    def clean(self):
        cleanedData = super(RegisterForm, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        logging.debug("Cleaned")
        if password != confirm:
            raise forms.ValidationError("Your passwords don't match.")
        
        if User.objects.filter(emailaddress__iexact=cleanedData.get("emailaddress")).exists():
            raise forms.ValidationError("Username taken")