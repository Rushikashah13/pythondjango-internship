from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('welcome to django')

def contactpageview(request):
    return HttpResponse('welcome to contact')

def aboutuspageview(request):
    return HttpResponse('welcome to aboutus')

