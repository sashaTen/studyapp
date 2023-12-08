from django.urls import path
from .views import hello ,    about

urlpatterns = [
    
    path('', hello, name='hello'),
    path('about/' , about ,  name='about')
]



