from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, "hotelmanagement/index.html")


def about(request):
    #return HttpResponse("hi this is giri")
    return render(request, "hotelmanagement/about.html")
    #return HttpResponseRedirect(reverse("hotelmanagement:index"))


def contact(request):
        print(request.POST)
        return render(request, "hotelmanagement/contact.html")


def details(request):
    if request.method == "POST":
        #return HttpResponse("you should render  all details to html page.")
        return render(request,"hotelmanagement/details.html")




