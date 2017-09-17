import logging
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import LoginForm, LoginModel, RegisterForm, RegisterForm2
from .models import UserType

# Create your views here.
def index(request):
    return render(request, 'auscities/index.html')

def login(request):
        form = LoginModel(request.POST or None)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/auscities/')
        return render(request, 'auscities/login.html/', {'form':form})

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/auscities/')
    return render(request, 'auscities/register.html', {'form':form})

def register2(request):
    form = RegisterForm2(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/auscities/')
    return render(request, 'auscities/register.html', {'form':form})
