from django.conf.urls import patterns, url

from pedido import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)