from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def shop_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(shop_home)
        
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    return redirect(shop_login)

def shop_home(req):
    return render(req,'shop/home.html')

