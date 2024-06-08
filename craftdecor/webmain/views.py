from django.shortcuts import render, get_object_or_404
from webadmin.models import Categories,Products
from django.db.models import Q

def index(request):
    cats = Categories.objects.filter(is_avail=True)
    catsft = Categories.objects.filter(is_avail=True)[:6]
    pros = Products.objects.filter(Q(is_avail=True) & Q(is_featured=True))
    return render(request, 'webmain/index.html',{'cats':cats,'pros':pros,'catsft':catsft})

def products(request):
    cats = Categories.objects.prefetch_related('items').filter(is_avail='True')
    catsft = Categories.objects.filter(is_avail=True)[:6]
    return render(request, 'webmain/products.html',{'cats':cats,'catsft':catsft})


def products_cat(request, cat_id):
    cats = Categories.objects.filter(is_avail=True)
    cat = get_object_or_404(Categories, id=cat_id)
    catsft = Categories.objects.filter(is_avail=True)[:6]
    pros = cat.items.all()
    return render(request, 'webmain/products_cat.html',{'cat':cat,'pros':pros,'cats':cats,'catsft':catsft})

def about(request):
    catsft = Categories.objects.filter(is_avail=True)[:6]
    return render(request,'webmain/about.html',{'catsft':catsft})

def history(request):
    catsft = Categories.objects.filter(is_avail=True)[:6]
    return render(request,'webmain/history.html',{'catsft':catsft})

def contact(request):
    catsft = Categories.objects.filter(is_avail=True)[:6]
    return render(request,'webmain/contact.html',{'catsft':catsft})
