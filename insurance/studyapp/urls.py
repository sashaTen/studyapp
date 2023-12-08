from django.urls import path
from .views import hello ,    about , goal

urlpatterns = [
    
    path('', hello, name='hello'),
    path('about/' , about ,  name='about'),
    path('goal/' ,   goal  ,  name   =  'goal')
]





