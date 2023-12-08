from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")




def  about(request):
    return HttpResponse('this  is the   small  text   about  the  study  app   it   serves   to  assist  in  learning   languages ')



def  goal(request):
    return   HttpResponse('our   goal  is to build   system  that   helps you  to  learn  efficiently  in  pleasurable way ')


def  userpage(request):
    return HttpResponse('user  information ')