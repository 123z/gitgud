import logging
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import hashers
from django.db.models import Q

from .forms import LoginModel, RegisterForm, AdminModel, EditProfile, CreateAdmin, SearchForm
from .models import UserType, User, Location, Admin

# Create your views here.
def help(request):
    return render(request, 'auscities/help.html')

def about(request):
    return render(request, 'auscities/about.html')

def Businessman(request):
    Businessman_hotel = Location.objects.filter(locationtype = 'hotel')
    Businessman_industry = Location.objects.filter(locationtype = 'industry')
    location_info = Location.objects.all()
	
	
    context = {
        'Businessman_hotel': Businessman_hotel,
        'Businessman_industry': Businessman_industry,
        'location_info': location_info,
		
    }
    return render(request, 'auscities/Businessman.html', context)
	
def Tourist(request):
	Tourist_hotel = Location.objects.filter(locationtype = 'hotel')
	location_info = Location.objects.all()
	context = {
		'Tourist_hotel': Tourist_hotel,
                'location_info': location_info,
		
	}
	return render(request, 'auscities/Tourist.html', context)
	
def Student(request):
	Student_college = Location.objects.filter(locationtype = 'college')
	Student_library = Location.objects.filter(locationtype = 'library')
	location_info = Location.objects.all()
	context = {
		'Student_college': Student_college,
		'Student_library': Student_library,
                'location_info': location_info,
	}
	return render(request, 'auscities/Student.html', context)

	

def index(request):
    return render(request, 'auscities/index.html')

def logout(request):

    if request.session['remember']:
        del request.session['logged']
        del request.session['type']
    else:
        request.session.flush()
    return HttpResponseRedirect('/')

def createadmin(request):
    form = CreateAdmin(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.password = hashers.make_password(instance.password)
        instance.save()
    return render(request, 'auscities/admincreate.html/', {'form':form})

def admin(request):
    form = AdminModel(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        admin = Admin.objects.get(emailaddress__iexact=instance.emailaddress)
        request.session['logged'] = 2
        return HttpResponseRedirect('/')
    return render(request, 'auscities/admin.html/', {'form':form})

def login(request):
        form = LoginModel(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = User.objects.get(emailaddress__iexact=instance.emailaddress)
            request.session['logged'] = 1
            request.session['user'] = user.emailaddress
            request.session['type'] = user.usertype
            if form.cleaned_data["rememberMe"]:
                request.session['remember'] = True
            else:
                request.session['remember'] = False
            logging.debug(form.cleaned_data["rememberMe"])
            return HttpResponseRedirect('/')
        else:
            try:
                if request.session['remember']:
                    form.fields['emailaddress'].initial = request.session['user']
                    form.fields['rememberMe'].initial = True
            except:
                pass
        return render(request, 'auscities/login.html/', {'form':form})

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        request.session['logged'] = 1
        request.session['user'] = user.emailaddress
        request.session['type'] = user.usertype
        request.session['remember'] = False
        user.password = hashers.make_password(user.password)
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'auscities/register.html', {'form':form})

def user(request):
    form = EditProfile(request.POST or None)
    if form.is_valid():
        user = User.objects.get(emailaddress__iexact=request.session['user'])
        user.firstname = form.cleaned_data['firstname']
        user.lastname = form.cleaned_data['lastname']
        user.password = hashers.make_password(form.cleaned_data['password'])
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'auscities/editprofile.html', {'form':form})


def result(request):
    location_info = Location.objects.all()
    context = {
        'location_info': location_info,
    }
    return render(request, 'auscities/result.html', context)
	
def location(request, id):
	info = Location.objects.get(locationid=id)
	history_tabs = Location.objects.all()
	context = {
        'info': info,
		'history_tabs': history_tabs,
    }
	return render(request, 'auscities/location.html', context)
	
def searched(request):
	global filtered, lname, lcity, ltype
	bool = True
	form = SearchForm(request.POST)
	if form.is_valid():
		lname = form.cleaned_data['Name']
		lcity = form.cleaned_data['City']
		ltype = form.cleaned_data['Type']
		if lname == "" and lcity == "" and ltype == "":
			bool = False
		filtered = Location.objects.filter(Q(name=lname) | Q(city=lcity) | Q(locationtype=ltype))
		form = SearchForm()
	context = {
		'filtered': filtered,
		'form': form,
		'bool': bool,
	}
	return render(request, 'auscities/result.html', context)
