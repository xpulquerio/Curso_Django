from django.shortcuts import render


def home(request):
    #return HttpResponse('Olá, internet')
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

