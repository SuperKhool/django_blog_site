from django.urls import path 
from .views import *
urlpatterns=[
    path('',dashboard,name='dashboard'),
    
    #Crud Category 
    path('categorys/',categorys,name='categorys'),
    path('categorys/add',add_categorys,name="add_categorys"),
    path('categorys/edit/<int:id>/',edit_categorys,name="edit_categorys"),
    path('<int:id>/',delete_categorys,name="delete_categorys"),
    
    #Crud Post
    path('posts/',posts,name='posts'),
    path('posts/add/',add_posts,name="add_posts"),
    path('posts/edit/<int:pk>/',edit_post,name='edit_post'),
    path('posts/delete/<int:pk>/',delete_post,name="delete_post"),

]