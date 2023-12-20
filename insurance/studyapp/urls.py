from django.urls import path
from .views import hello ,    about ,  userpage, courses ,  FAQ

urlpatterns = [
    
    path('', hello, name='hello'),
    path('about/' , about ,  name='about'),
    path('courses/'  ,   courses ,  name='courses') , 
    path('userpage' ,     userpage  ,  name='userpage'),
    path('faq/' ,     FAQ ,    name="FAQ")
]





