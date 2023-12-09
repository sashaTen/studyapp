from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")




def  about(request):
    #return HttpResponse('this  is the   small  text   about  the  study  app   it   serves   to  assist  in  learning   languages ')
    return  render(request , "about.html")



def  goal(request):
    #return   HttpResponse('our   goal  is to build   system  that   helps you  to  learn  efficiently  in  pleasurable way ')
    return  render(request,    "goal.html")


def  userpage(request):
    return  render(request ,   "userpage.html")



def   courses(request):
    return   render(request  ,   "courses.html")