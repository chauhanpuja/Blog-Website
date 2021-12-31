from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import Comment, Contact, Product,Order
from math import ceil
from django.contrib import messages


# Create your views here.
def home(request):
    products=Product.objects.all()
    params={'products':products}
    return render(request,'home.html',params)


def register(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        password2=request.POST.get('password2','')
        
        if(password==password2):
            if User.objects.filter(username=username).exists(): 
                messages.error(request,'username has been already taken')
                return redirect('/shop') 
            elif User.objects.filter(email=email).exists(): 
                messages.error(request,'email has been taken')
                return redirect('/shop') 
            else:
                # create the user
                myuser=User.objects.create_user(username,email,password)
                myuser.first_name=first_name
                myuser.last_name=last_name
                myuser.save()
                messages.success(request,'user created')
                return redirect('/shop')    
                
        else:
            messages.error(request,'password is not matching')
            return redirect('/shop') 
    else:
        return HttpResponse("404 - Not found")  
        
    return render(request,'/shop')
   
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successfully logged In')
            return redirect('/shop')

        else:
            messages.error(request,'User not Signup')
            return redirect('/shop') 
    return render(request,'/shop')


def userlogout(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect("/shop")


def checkout(request):
    return render(request,'checkout.html')

def comments(request):
    if request.method=="POST":
        comments=request.POST.get('comment')
        user=request.user
        comment=Comment(comments=comments,user=user)
        comment.save()
        messages.info(request,"Comment Succesfully Added")
    text=Comment.objects.all
    return render(request,'comment.html',{'comments':text})

def contact(request):
    if request.method=='POST': 
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')

        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.info(request,"Message Sent Successfully")
    return render(request,'contact.html')

def quickview(request,id):
    products=Product.objects.filter(id=id)
    return render(request,'quickview.html',{'product':products})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()

        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')

