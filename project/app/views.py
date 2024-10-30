from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

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
    a=[{'name':'roshan','age':21},{'name':'sajan','age':24},{'name':'jith','age':20},{'name':'aromal','age':22}]
    return render(req,'demo.html',{'data':a})

users=[{'id':'21','name':'john','age':'25','email':'j@gmail.com'},{'id':'22','name':'cena','age':'30','email':'c@gmail.com'},{'id':'23','name':'brock','age':'30','email':'b@gmail.com'}]

def display(req):
    return render(req,'display_user.html',{'users':users})

def user_reg(req):
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        users.append({'id':id,'name':name,'age':age,'email':email})
        return redirect(display)
    
def edit_user(req,id):
    user=''
    for i in users:
        if i['id']==id:
            user=i
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        user['id']=id
        user['name']=name
        user['age']=age
        user['email']=email
        return redirect(display)
    
    return render(req,'edit_user.html',{'user':user})

def delete_user(req,id):
    for i in users:
        if i['id']==id:
            users.remove(i)
    return redirect(display)

def display_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'std':data})

def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        data=Student.objects.create(roll_no=roll,name=name,age=age,email=email)
        data.save()
        return redirect(display_std)
    else:
        return render(req,'add_std.html')
    
def edit_std(req,id):
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,email=email)
        return redirect(display_std)
    return render(req,'edit_std.html',{'data':data})

def delete_std(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(display_std)


