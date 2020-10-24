from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #quando for vazio, vou chamar a view index
]