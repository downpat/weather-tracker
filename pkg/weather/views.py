from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from weather.models import City, UserCity

def index(request):
    context = {}
    if request.user.is_authenticated:
        user_cities = UserCity.objects.filter(user=request.user)
        context['user_cities'] = user_cities
    
    if request.method == 'POST':
        cities = City.objects.filter(name__icontains=request.POST['search'])
        context['cities'] = cities
    
    return render(request, 'index.html', context)

def city(request, city_id):
    city = City.objects.get(pk=city_id)
    
    users_city = False
    if request.user.is_authenticated:
        users_city = UserCity.objects.filter(user=request.user, city__pk=city_id).exists()
    return render(request, 'city.html', {'city': city, 'users_city':users_city})

def add_city(request, city_id):
    if request.user.is_authenticated:
        UserCity.objects.get_or_create(city=City.objects.get(pk=city_id), user=request.user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))

def remove_city(request, city_id):
    if request.user.is_authenticated:
        UserCity.objects.filter(city__pk=city_id, user=request.user).delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))

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
    return HttpResponseRedirect(reverse('index'))
