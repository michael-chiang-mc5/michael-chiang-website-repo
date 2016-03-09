from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addEntryEditor/$', views.addEntryEditor, name='addEntryEditor'),
    url(r'^addEntry/$', views.addEntry, name='addEntry'),
    url(r'^editEntryEditor/(?P<blogEntry_pk>[0-9]+)/$', views.editEntryEditor, name='editEntryEditor'),
    url(r'^editEntry/(?P<blogEntry_pk>[0-9]+)/$', views.editEntry, name='editEntry'),
    url(r'^hideEntry/(?P<blogEntry_pk>[0-9]+)/$', views.hideEntry, name='hideEntry'),
    url(r'^unhideEntry/(?P<blogEntry_pk>[0-9]+)/$', views.unhideEntry, name='unhideEntry'),


    url(r'^adminPanel/$', views.adminPanel, name='adminPanel'),

]
