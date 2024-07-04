from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404

from Dashboard.forms import CategoryForm
from blogs.models import Blog, category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=('login'))
def dashboard(request):
    category_count=category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request,'dashboard/dashboard.html',context)


def categorys(request):
    return render(request,'dashboard/categorys.html')

def add_categorys(request):
    
    if request.method=='POST':
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorys')    
    form =CategoryForm()   
    context={
        'form':form
    }
    return render(request,'dashboard/add_categorys.html',context)


def edit_categorys(request,id):
    edit_categorys=get_object_or_404(category,id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=edit_categorys)
        if form.is_valid():
            form.save()
            return redirect('categorys')    
    form = CategoryForm(instance=edit_categorys)
    context={
        'edit_categorys':edit_categorys,
        'form':form
    }
    return render(request,'dashboard/edit_categorys.html',context)




def delete_categorys(request,id):
    delete_cat=get_object_or_404(category,id=id)
    delete_cat.delete()
    return redirect('categorys')
    