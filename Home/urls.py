
from django.urls import path
from .views import *


urlpatterns = [
   path('', home, name='home'),
   path('add', addphotos, name='addphotos'),
   path('photov/<str:pk>/',photov, name='photov'),
   path('deletev/<str:pk>/',deletev, name='deletev'),
   path('deletecat/<str:pk>/',deletecat, name='deletecat'),
]