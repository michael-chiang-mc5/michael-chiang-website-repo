from django.shortcuts import render
from MCEditor.views import editor
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    blogEntries = BlogEntry.objects.filter(hidden=False)
    context = {'blogEntries':blogEntries,}
    return render(request, 'Blog/index.html', context)

def adminPanel(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    blogEntries = BlogEntry.objects.all()
    context = {'blogEntries':blogEntries,}
    return render(request, 'Blog/adminPanel.html', context)

def addEntryEditor(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    submit_url = reverse('Blog:addEntry')
    form_data = {}
    header = "Add a blog post"
    initial_text = ""
    html = editor(request,submit_url,form_data,header,initial_text) # See MCEditor.views
    return html
def addEntry(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    form_text = request.POST.get("form-text")
    blogEntry = BlogEntry(text=form_text)
    blogEntry.save()
    return HttpResponseRedirect( reverse('Blog:adminPanel') )

def editEntryEditor(request,blogEntry_pk):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    submit_url = reverse('Blog:editEntry',args=[blogEntry_pk])
    form_data = {}
    header = "Edit a blog post"
    initial_text = BlogEntry.objects.get(pk=blogEntry_pk).text
    html = editor(request,submit_url,form_data,header,initial_text) # See MCEditor.views
    return html
def editEntry(request,blogEntry_pk):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    form_text = request.POST.get("form-text")
    blogEntry = BlogEntry.objects.get(pk=blogEntry_pk)
    blogEntry.text = form_text
    blogEntry.save()
    return HttpResponseRedirect( reverse('Blog:adminPanel') )

def hideEntry(request,blogEntry_pk):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    blogEntry = BlogEntry.objects.get(pk=blogEntry_pk)
    blogEntry.hidden=True
    blogEntry.save()
    return HttpResponseRedirect( reverse('Blog:adminPanel') )
def unhideEntry(request,blogEntry_pk):
    if not request.user.is_superuser:
        return HttpResponse("You are not a superuser")
    blogEntry = BlogEntry.objects.get(pk=blogEntry_pk)
    blogEntry.hidden=False
    blogEntry.save()
    return HttpResponseRedirect( reverse('Blog:adminPanel') )
