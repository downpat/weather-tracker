from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^city/(?P<city_id>[0-9]*)/$', views.city, name='city'),
    url(r'^city/(?P<city_id>[0-9]*)/add/$', views.add_city, name='add_city'),
    url(r'^city/(?P<city_id>[0-9]*)/remove/$', views.remove_city, name='remove_city'),
    url(r'^user/cities/', views.user_cities, name='user_cities'),
    url(r'^accounts/profile/', views.uc_redirect),
    url(r'^logout/', views.weather_logout, name='weather_logout'),
    url(r'^', include('django.contrib.auth.urls')),
]
