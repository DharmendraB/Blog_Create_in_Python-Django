from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.blogHome, name="BlogHome" ),
    path('<int:id>/<str:slug>',views.blogPost, name="BlogPost" )
]