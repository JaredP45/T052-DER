from django.urls import path
from . import views

app_name = "main" 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('data', views.data, name='data'),
    path('contact', views.contact, name='contact'),
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path("register", views.admin_register, name="register")
]
