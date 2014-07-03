from django.conf.urls import patterns, url

from Empresa import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)