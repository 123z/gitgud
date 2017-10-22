import logging
from django import forms
from django.forms import ModelForm
from django.contrib.auth import hashers


from .models import User, Admin
#Model form for use of databases elements in the form
class CreateAdmin(ModelForm):
    confirm = forms.CharField(label ='Confirm password',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password...'}))
    class Meta:
        model = Admin
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
            }
        
    def clean(self):
        cleanedData = super(CreateAdmin, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        logging.debug("Cleaned")
        if password != confirm:
            raise forms.ValidationError("Your passwords don't match.")
        
        if Admin.objects.filter(emailaddress__iexact=cleanedData.get("emailaddress")).exists():
            raise forms.ValidationError("Username taken")
        
class AdminModel(ModelForm):
    #rememberMe = forms.BooleanField(label="Remember me", required=False)
    class Meta:
        model = Admin
        fields = ['emailaddress', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder':'Enter your password...'}),
                    'emailaddress': forms.TextInput(attrs={'placeholder':'Enter your username...'}),
            }
        labels = {
                'emailaddress': 'E-mail address',
            }
    def clean(self):
        cleanedData = super(AdminModel, self).clean()
        cUsername = cleanedData.get("emailaddress")
        try:
            admin = Admin.objects.get(emailaddress__iexact=cUsername)
            if hashers.check_password(cleanedData.get("password"), admin.password):
                logging.debug("test")
            else:
                raise forms.ValidationError("Username or password incorrect")
        except User.DoesNotExist:
            raise forms.ValidationError("Username or password incorrect")
            
class LoginModel(ModelForm):
    rememberMe = forms.BooleanField(label="Remember me", required=False)
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
                logging.debug(cleanedData.get("rememberMe"))
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

class EditProfile(forms.Form):
    firstname = forms.CharField(label = 'Enter your first name.',
                                widget=forms.TextInput(attrs={'placeholder':'Enter your first name...'}))
    lastname = forms.CharField(label = 'Enter your last name.',
                                widget=forms.TextInput(attrs={'placeholder':'Enter your last name...'}))
    password = forms.CharField(label ='Enter your password',
                              widget=forms.PasswordInput(attrs={'placeholder':'Enter your password...'}))
    confirm = forms.CharField(label ='Confirm password',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your password...'}))

    def clean(self):
        cleanedData = super(EditProfile, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        logging.debug("Cleaned")
        if password != confirm:
            raise forms.ValidationError("Your passwords don't match.")
