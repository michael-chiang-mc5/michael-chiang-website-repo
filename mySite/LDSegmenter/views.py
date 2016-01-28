from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'LDSegmenter/index.html', context)

def tutorial(request):
    context = {}
    return render(request, 'LDSegmenter/tutorial.html', context)
