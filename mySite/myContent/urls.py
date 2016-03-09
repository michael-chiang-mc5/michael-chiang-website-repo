from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^software/$', views.software, name='software'),
    url(r'^contact/$', views.contact, name='contact'),
]
