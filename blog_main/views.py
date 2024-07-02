from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import category ,Blog
from .forms import RegForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 

def home(request):   
    category_list=category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status="Published").order_by('updated_at')
    simple_post=Blog.objects.filter(is_featured=False,status="Published" ).order_by('updated_at')
    context={
        
        'category_list':category_list,
        'featured_post':featured_post,
        'simple_post':simple_post
            
    }
    return render(request,'home.html',context)

def register(request):
    if request.method == 'POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register') 
        else:
            return HttpResponse("Please Provide Valid Information!")  
    else:
        form=RegForm()
    context={
        'form':form
    }
    return render(request,'registration.html',context)


def login(request):
    
    if request.method == 'POST':
        login_form=AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return redirect('register')
        
    else:
        login_form=AuthenticationForm()   
    context={
        'login_form':login_form 
    }
    return render(request,'login.html',context)


def logout(requset):
    auth.logout(requset)
    return redirect('home')