from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("welcome")

def demo1(request,a):
    # a=input('enter an item : ')
    return HttpResponse(a)

def bonus(request,a,b):
    if b>5:
        c=0.05*a
        return HttpResponse(c)
    else:
        return HttpResponse('no change')

def monument(request,a):
    if a=='delhi':
        return HttpResponse('Redfort')
    elif a=='agra':
        return HttpResponse('Tajmahal')
    elif a=='kerala':
        return HttpResponse('varkala')
    else:
        return HttpResponse('invalid')

def div(request,a):
    b=a%10
    if b%3==0:
        return HttpResponse('true')
    else:
        return HttpResponse('false')
    
def day(request,a):
    if a==1:
        return HttpResponse('Sunday')
    elif a==2:
        return HttpResponse('monday')
    elif a==3:
        return HttpResponse('Tuesday')
    elif a==4:
        return HttpResponse('wednesday')
    elif a==5:
        return HttpResponse('Thursday')
    elif a==6:
        return HttpResponse('Friday')
    elif a==7:
        return HttpResponse('saturday')
    else:
        return HttpResponse('invalid')
    
def tax(request,a):
    if a>100000:
        b=a*15/100
        total=a+b
        return HttpResponse(total)
    elif a>50000 and a<=100000:
        b=a*10/100
        total=a+b
        return HttpResponse(total)
    else:
        b=a*5/100
        total=a+b
        return HttpResponse(total)
    
def elec(request,a):
    if a<100:
        return HttpResponse("Your unit price = 0")
    else:
        if a<200 and a>100:
            up=a-100
            ua=up*5
            return HttpResponse(ua)
        else:
            ui=a-200
            us=ui*10+500
            return HttpResponse(us)
        
def demo(req):
    a={'name':'roshan','age':21}
    return render(req,'demo.html',{'data':a})

