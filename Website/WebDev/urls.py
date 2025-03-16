from . import views
from django.contrib import admin  
from django.urls import path       
from django.conf import settings   

urlpatterns = [                               
    path('', views.home, name ='home'),                                      # home page
    path('Developers', views.devs, name ='devs'),                            # dev page
    path('client_dashboard', views.client_dash, name ='client_dash'),        # client dash
    path('login', views.login_page, name='login'),                           # Login page
    path('register', views.register_page, name='register'),                  # Registration page
    path('admin_login', views.admin_login, name='admin_login'),              # admin login
    path('admin_dashboard', views.admin_dash, name='admin_dashboard'),
    path('client_website_details', views.client_website_details, name='client_website_details'),  # website details
    path('admin_website_details', views.admin_website_details, name='admin_website_details'),  # website details
    path('admin_billing', views.admin_billing, name='admin_billing'),  # website details
     path('client_billing', views.client_billing, name='client_billing'),  # website details

]



