from django.urls import path
from .views import hello ,    about ,  userpage, courses

urlpatterns = [
    
    path('', hello, name='hello'),
    path('about/' , about ,  name='about'),
    path('courses/'  ,   courses ,  name='courses') , 
    path('userpage' ,     userpage  ,  name='userpage')
]





