from django.shortcuts import render, redirect
from blogs.models import category ,Blog

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
