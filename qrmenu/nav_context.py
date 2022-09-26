from products.models import Category,STATUS

def nav_data(request):
    context = dict()
    
    context['categories'] = Category.objects.filter(
        status="published"
    ).order_by('title')
    
    return context