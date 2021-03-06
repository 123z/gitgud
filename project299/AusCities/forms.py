import logging
from django import forms
from django.forms import ModelForm
from django.contrib.auth import hashers
from django.db.models import Q

from .models import User, Admin, Location
#Model form for use of databases elements in the form

class AddInfo(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
                'emailaddress': forms.EmailInput(attrs={'placeholder':'Enter a valid e-mail.'}),
                'name': forms.TextInput(attrs={'placeholder':'Enter a valid location name.'}),
                'address': forms.TextInput(attrs={'placeholder':'Enter a valid address.'}),
                'city': forms.TextInput(attrs={'placeholder':'Enter a valid city.'}),
                'phonenumber': forms.TextInput(attrs={'placeholder':'Enter a valid phone number.'}),
                'website': forms.URLInput(attrs={'placeholder':'Enter a valid website address.'}),
            }
        labels = {
                'emailaddress': 'E-mail address',
                'name': 'Location name',
                'phonenumber': 'Phone number',
                'locationtype': 'Location type',
            }

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
    firstname = forms.CharField(label = 'Update user first name.',
                                widget=forms.TextInput(attrs={'placeholder':'Enter your new first name...'}))
    lastname = forms.CharField(label = 'Update user last name.',
                                widget=forms.TextInput(attrs={'placeholder':'Enter your new last name...'}))
    password = forms.CharField(label ='New password',
                              widget=forms.PasswordInput(attrs={'placeholder':'Enter your new password...'}))
    confirm = forms.CharField(label ='Confirm new password',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter your new password...'}))


    def clean(self):
        cleanedData = super(EditProfile, self).clean()
        password = cleanedData.get("password")
        confirm = cleanedData.get("confirm")
        logging.debug("Cleaned")
        if password != confirm:
            raise forms.ValidationError("Your passwords don't match.")
			
class SearchForm(forms.Form):

	Name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Name'}))
	City = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'City'}))
	Type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Location Type'}))
	
	def clean(self):
		cleanedData = super(SearchForm, self).clean()
		Name = cleanedData.get("Name")
		City = cleanedData.get("City")
		Type = cleanedData.get("Type")
		
		if not Name and not City and not Type:
			raise forms.ValidationError("You need to enter something to search for a location")
			
		try:
			Location.objects.get(name=Name)
		except Location.DoesNotExist:
			try:
				Location.objects.filter(city=City)[:1].get()
			except Location.DoesNotExist:
				try:
					Location.objects.filter(locationtype=Type)[:1].get()
				except Location.DoesNotExist:
					raise forms.ValidationError("No locations match your search")
			