from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,'home.html')

def contactpageview(request):
    return render(request,'contact.html')

def aboutuspageview(request):
    return render(request,'aboutus.html')

