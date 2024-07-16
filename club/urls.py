from django.contrib import admin
from django.urls import path
from club import views

urlpatterns = [
    path("",views.index,name='home'),
    path("core.html",views.core_team_view, name='core'),
    path("core",views.core_team_view, name='core'),
    path("dance.html",views.dance, name='dance'),
    path("dance",views.dance, name='dance'),
    path("music.html",views.music, name='music'),
    path("music/",views.music, name='music'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("gallery",views.gallery, name='gallery'),
]