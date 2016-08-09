from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# Create your views here.

def home(request):
	context = {
	
	}
	return render(request, "home.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/dashboard/")# Redirect to a success page.
    return render(request, 'login.html', {'form': form })

@login_required
def Dashboard(request):
    context = {

    }
    return render(request, 'index.html', context)
