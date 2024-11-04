from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os

# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname
            return redirect(shop_home)
        
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    req.session.flush()
    logout(req)
    return redirect(shop_login)

def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()[::-1][:10]
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(shop_login)

def add_pro(req):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            des=req.POST['des']
            img=req.FILES['img']
            data=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,dis=des,img=img)
            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_pro.html')
    else:
        return redirect(shop_login)
    
def edit_product(req,pid):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            des=req.POST['des']
            img=req.FILES['img']
            if img:
                Product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,dis=des,img=img)
            else:
                Product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,dis=des)

            return redirect(shop_home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit.html',{'product':data})
    else:
        return redirect(shop_login)





            # data=Product.objects.get(pk=pid)
            # url=data.img.url
            # og_path=url.split('/')[-1]
            # os.remove('media/'+og_path)
            # data.delete()
            # print(og_path)
            # return redirect(shop_home)






