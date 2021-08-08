from django.urls import path
from hotelmanagement import views


app_name = 'hotelmanagement'
urlpatterns  = [
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("details/", views.details, name="details"),

]