
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import LoginForm, UserForm
from .models import UserType

# Create your views here.
def index(request):
    return render(request, 'auscities/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user1 = form.cleaned_data['user']
            password = form.cleaned_data['password']
            return render(request, 'auscities/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'auscities/login.html', {'form': form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/auscities/')
    return render(request, 'auscities/register.html', {'form':form})
