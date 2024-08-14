from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def forPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'for_test.html', context)

def forGard(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'gard.html', context)

def cardColorPage(request):
    context = {
        'color': 'all',
    }
    if request.method == "GET" and request.GET.get('color') != None:
        context['color'] = request.GET['color']
    return render(request, 'card_color.html', context)

def forFormSend(request):
    email = ""
    password = ""

    context = {}

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('my-password')

    context['email'] = email
    context['password'] = password

    return render(request, 'sendform.html', context)