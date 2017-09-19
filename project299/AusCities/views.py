import logging
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import LoginModel, RegisterForm, RegisterForm2
from .models import UserType

# Create your views here.
def index(request):
    return render(request, 'auscities/index.html')

def logout(request):
    request.session.delete()
    return HttpResponseRedirect('/auscities/')

def login(request):
        form = LoginModel(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = User.objects.get(username__iexact=instance.username)
            request.session['logged'] = 1
            request.session['user'] = user.username
            request.session['type'] = user.userType.__str__()
            logging.debug(request.session['type'])
            return HttpResponseRedirect('/auscities/')
        return render(request, 'auscities/login.html/', {'form':form})

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        request.session['logged'] = 1
        request.session['user'] = user.username
        request.session['type'] = user.userType.__str__()
        user.password = hashers.make_password(user.password)
        user.save()
        return HttpResponseRedirect('/auscities/')
    return render(request, 'auscities/register.html', {'form':form})

def register2(request):
    form = RegisterForm2(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/auscities/')
    return render(request, 'auscities/register.html', {'form':form})
