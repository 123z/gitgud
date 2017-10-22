import logging
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import hashers

from .forms import LoginModel, RegisterForm
from .models import UserType, User, Location

# Create your views here.
def help(request):
    return render(request, 'auscities/help.html')

def about(request):
    return render(request, 'auscities/about.html')

def Businessman(request):
	Businessman_hotel = Location.objects.filter(locationtype = 'hotel')
	Businessman_industry = Location.objects.filter(locationtype = 'industry') 
	context = {
		'Businessman_hotel': Businessman_hotel,
		'Businessman_industry': Businessman_industry,
	}
	return render(request, 'auscities/Businessman.html', context)
	
def Tourist(request):
	Tourist_hotel = Location.objects.filter(locationtype = 'hotel')
	context = {
		'Tourist_hotel': Tourist_hotel,
		
	}
	return render(request, 'auscities/Tourist.html', context)
	
def Student(request):
	Student_college = Location.objects.filter(locationtype = 'college')
	Student_library = Location.objects.filter(locationtype = 'library') 
	context = {
		'Student_college': Student_college,
		'Student_library': Student_library,
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
