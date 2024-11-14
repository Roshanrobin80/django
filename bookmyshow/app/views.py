from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(req):
    return render(req,'index.html')

def arm(req):
    return render(req,'arm.html')