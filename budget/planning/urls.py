from django.conf.urls import url

from . import views

urlpatterns = [

    #Homepage
    url(r'^$', views.index, name='header'),

]