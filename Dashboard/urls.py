from django.urls import path 
from .views import *
urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('categorys/',categorys,name='categorys'),
    path('categorys/add',add_categorys,name="add_categorys"),
    path('categorys/edit/<int:id>/',edit_categorys,name="edit_categorys"),
    path('<int:id>/',delete_categorys,name="delete_categorys")

]