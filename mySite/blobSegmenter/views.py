from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'blobSegmenter/index.html', context)

def tutorial(request):
    context = {}
    return render(request, 'blobSegmenter/tutorial.html', context)
