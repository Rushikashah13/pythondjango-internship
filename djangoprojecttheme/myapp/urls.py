from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('contact',views.contactpageview,name="contact"),
    path('aboutus',views.aboutuspageview,name="aboutus"),
]