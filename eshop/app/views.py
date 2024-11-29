from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"invalid username or password")
            return redirect(shop_login)
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
    
#-------------------------------admin-----------------------------


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




def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    print(og_path)
    return redirect(shop_home)



#----------------------------------user----------------------------



def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            send_mail('user registration', 'eshop created', settings.EMAIL_HOST_USER, [email])        
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,"email not valid")
            return redirect(register)
    else:
        return render(req,'user/register.html')
    
def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'data':data})
    else:
        return redirect(shop_login)
    
def view_pro(req,pid):
    data=Product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})

def add_to_cart(req,pid):
    product=Product.objects.get(pk=pid)
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.create(user=user,product=product)
    data.save()
    return redirect(view_cart)

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    cart_dtls=Cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart_dtls':cart_dtls})

def delete_cart(req,id):
    cart=Cart.objects.get(pk=id)
    cart.delete()
    return redirect(view_cart)

#cart buy

def user_buy(req,cid):
    user=User.objects.get(username=req.session['user'])
    cart=Cart.objects.get(pk=cid)
    product=cart.product
    price=cart.product.offer_price
    buy=Buy.objects.create(user=user,product=product,price=price)
    buy.save()
    cart.delete()
    return redirect(view_cart)

#product buy

def user_buy1(req,pid):
    user=User.objects.get(username=req.session['user'])
    product=Product.objects.get(pk=pid)
    price=product.offer_price
    buy=Buy.objects.create(user=user,product=product,price=price)
    buy.save()
    return redirect(user_home)

def user_bookings(req):
    user=User.objects.get(username=req.session['user'])
    buy=Buy.objects.filter(user=user)[::-1]
    return render(req,'user/bookings.html',{'buy':buy})





