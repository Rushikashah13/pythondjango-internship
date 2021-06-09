from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('contact',views.contactpageview,name="contact"),
    path('aboutus',views.aboutuspageview,name="aboutus"),
    path('form',views.myform,name="myform"),
    path('formprocess',views.process,name="process"),
    
]