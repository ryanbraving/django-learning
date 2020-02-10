# from django.conf.urls import url
from django.urls import path
from first_app import views


urlpatterns = [
    # url(r'^$', views.index, name='index')
    path('', views.first_app, name='first_app')
]
