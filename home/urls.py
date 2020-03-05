from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="Home" ),
    path("home", views.index, name="Home" ),
    path("contact/",views.contact, name="ContactUs" ),
    path("about/",views.about, name="AboutUs" ),
    path("privacy/",views.privacy, name="privacy" ),
    path("search/",views.search, name="Search" ),
    path("login",views.handelLogin, name="Login" ),
    path("logout/",views.handelLogout, name="LogOut" ),
    path("signup",views.handelSignUp, name="HendelSignUp" ),
]