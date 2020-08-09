from django.urls import path 

from .import views



urljobs = [
    path('',view.index,name="index")
    
]