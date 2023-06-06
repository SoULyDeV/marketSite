from django.shortcuts import render

from item.models import Item, Category

# Create your views here.
def index(request):
    #bellow we need to see the last 2 items added in all categories
    items = Item.objects.filter(is_sold=False)[0:2]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')