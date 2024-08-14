from django.urls import path
from . import views


urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutUs, name="about"),
    path("contact/", views.contact, name="contact"),
    path("for/", views.forPage, name="for-page"),
    path("gard/", views.forGard, name="gard"),
    path("color/", views.cardColorPage, name="color-page"),
    path("form/", views.forFormSend, name="form"),

]
