from django.urls import path
from . import views


urlpattterns=[
    path('^$',views.home,name='home'),
]