from django.urls import path
from . import views


urlpattterns=[
    path('^$',views.home,name='home'),
    path('profile/<int:id>/',views.profile,name='profile'), 
]