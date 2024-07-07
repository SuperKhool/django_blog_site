from django.contrib import admin
from .models import category 
from .models import Blog ,social_link,Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','status','created_at','updated_at','is_featured')
    search_fields = ['id','title','category__category_name','status']
    prepopulated_fields = {'slug':('title',)}
    list_editable=("is_featured",)

admin.site.register(category )
admin.site.register(Blog ,BlogAdmin)
admin.site.register(social_link)
admin.site.register(Comment)