from django.urls import path
from .views import ingresoAdoptante


urlpatterns = [
    path('ingresoAdoptante/', ingresoAdoptante, name='ingresoAdoptante')

]