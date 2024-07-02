from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return HttpResponse("Hello, This is my web page")


def aboutUs(request):
    return HttpResponse("เกี่ยวกับฉัน")_


def contact(request):
    return HttpResponse("ติดต่อฉัน")
