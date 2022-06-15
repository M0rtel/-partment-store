from django.urls import path
from . import views

urlpatterns = [
    path('rec', views.recommendation, name='rec'),
    path('atelier', views.atelier, name='atelier'),
    path('1flat', views.flat_1, name='1flat'),
    path('2flat', views.flat_2, name='2flat'),
    path('3flat', views.flat_3, name='3flat')
]
