from django.urls import path
from siteApp import views

app_name = 'siteApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
