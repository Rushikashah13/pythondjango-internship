from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,'home.html')

def contactpageview(request):
    return render(request,'contact.html')

def aboutuspageview(request):
    return render(request,'aboutus.html')

def myform(request):
    return render(request,'myform.html')


def process(request):
    print('welcome')
    print(request.method)
    print(request.POST)
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c = a + b
    print(c)
    return render(request,'ans.html', {'mya':a,'myb':b,'mysum':c}) 