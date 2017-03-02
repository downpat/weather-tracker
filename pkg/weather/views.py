from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from weather.models import City

def index(request):
    if request.method == 'POST':
        cities = City.objects.filter(name__icontains=request.POST['search'])
        return render(request, 'index.html', {'cities': cities})
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('user_cities'))

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def weather_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_cities(request):
    return HttpResponse("%s's cities!" % request.user.username)

def uc_redirect(request):
    return HttpResponseRedirect(reverse('user_cities'))
