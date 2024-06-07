from django.urls import path

from WetherApp import views

urlpatterns = [
    path('',views.homepage,name='home')
]