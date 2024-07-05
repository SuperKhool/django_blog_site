from django.shortcuts import render,HttpResponse ,redirect,get_object_or_404
from Dashboard.forms import AddUserForm, BlogPostForm, CategoryForm , EditUserForm
from blogs.models import Blog, category
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
#Load Category here
def categorys(request):
    return render(request,'dashboard/categorys.html')

#Add Category 
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

#Edit Category 
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

#Delete Category 

def delete_categorys(request,id):
    delete_cat=get_object_or_404(category,id=id)
    delete_cat.delete()
    return redirect('categorys')
    
    
def posts(request):
    post = Blog.objects.all()
    context = {
        'post':post
    }
    return render(request,'dashboard/posts.html',context)


def add_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)                       #Temporary Form Save !
            post.author = request.user
            post.save()                                          #Here we save the form to get the Pk/id
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)      #(Adding The Pk We are getiing pk bcz we save the form first )
            post.save()          #final save After The Slug setup
            return redirect('posts') 
        else:
            print("Form is invalid")
            print(form.errors)
    form = BlogPostForm()    
    context = {
        'form':form
    }
    return render(request,'dashboard/add_posts.html',context)

def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    form=BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post     
    }
    return render(request,'dashboard/edit_post.html',context)


def delete_post(request,pk):
    delete_post = get_object_or_404(Blog,pk=pk)
    delete_post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'dashboard/users.html',context)


def add_user(request):
    form = AddUserForm()
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print('Form is invalid')
            print(form.errors)     
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_user.html',context)


def edit_user(rquest,pk):
    edit_user = get_object_or_404(User,pk=pk)
    if rquest.method == 'POST':
        edit_user = EditUserForm(rquest.POST,instance=edit_user)
        if edit_user.is_valid():
            edit_user.save()
            return redirect('users')
        else:
            print("invalid Form")
            print(edit_user.errors)
    form = EditUserForm(instance=edit_user)
    context = {
        "form":form
    }
    return render(rquest,'dashboard/edit_user.html',context)



def delete_user(request,pk):
    delete_user = get_object_or_404(User,pk=pk)
    delete_user.delete()
    return redirect('users')