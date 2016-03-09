from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    #return render(request, 'myContent/index.html', context)
    return render(request, 'myContent/cv.html', context)

def cv(request):
    context = {}
    return render(request, 'myContent/cv.html', context)

def publications(request):
    context = {}
    return render(request, 'myContent/publications.html', context)

def software(request):
    context = {}
    return render(request, 'myContent/software.html', context)

def contact(request):
    context = {}
    return render(request, 'myContent/contact.html', context)
