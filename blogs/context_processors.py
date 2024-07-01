from .models import category  ,social_link

def category_list(request):
    category_list=category.objects.all()
    return dict(category_list=category_list)



def Social_Link(requset):
    social_links=social_link.objects.all()
    return dict(social_links=social_links)