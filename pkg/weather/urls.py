from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^user/cities/', views.user_cities, name='user_cities'),
    url(r'^accounts/profile/', views.uc_redirect),
    url(r'^logout/', views.weather_logout, name='weather_logout'),
    url(r'^', include('django.contrib.auth.urls')),
]
