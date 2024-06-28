from django.shortcuts import render,HttpResponse ,redirect
from .models import *
from . import models

def post_by_category(req,category_id):
    #fetch the data from category_id
    post=Blog.objects.filter(status="Published",category_id=category_id)

    try:
        categorys=category.objects.get(pk=category_id)
    except:
        return redirect('home')
        
    context={
        'post':post,
        'categorys':categorys,
    }
    return render(req,'post_by_category.html',context)