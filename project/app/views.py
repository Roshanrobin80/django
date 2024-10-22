from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(req):
    return HttpResponse('Patience is a virtue')
def fun2(reg,a,b):
    return HttpResponse(a,b)

