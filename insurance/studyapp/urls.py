from django.urls import path
from .views import hello ,    about , goal ,  userpage, courses

urlpatterns = [
    
    path('', hello, name='hello'),
    path('about/' , about ,  name='about'),
    path('courses/'  ,   courses ,  name='courses') , 
    path('goal/' ,   goal  ,  name   =  'goal'),
    path('userpage' ,     userpage  ,  name='userpage')
]





