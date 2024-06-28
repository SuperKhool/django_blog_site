from .models import category 

def category_list(request):
    category_list=category.objects.all()
    return dict(category_list=category_list)