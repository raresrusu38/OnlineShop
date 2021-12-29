from django.shortcuts import get_object_or_404, render
from .models import Product, Categories, Price_Filter, Color, Brand
from django.db.models import Count

# Create your views here.


def home(request):
    products = Product.objects.filter(status='Published').order_by('id')
    
    context = {
        'products' : products,
    }
    
    return render(request, 'store_app/index.html', context)


def all_products(request):
    products = Product.objects.filter(status='Published').order_by('id')
    categories = Categories.objects.all()
    price_filter = Price_Filter.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    cat_id = request.GET.get('categories')
    price_filter_id = request.GET.get('price_filter')
    color_id = request.GET.get('color')
    brand_id = request.GET.get('brand')
    
    ATOZ_id = request.GET.get('ATOZ')
    ZTOA_id = request.GET.get('ZTOA')
    
    PRICE_LOW_TO_HIGH_id = request.GET.get('PRICE_LOW_TO_HIGH')
    PRICE_HIGH_TO_LOW_id = request.GET.get('PRICE_HIGH_TO_LOW')
    
    NEW_id = request.GET.get('NEW')
    USED_id = request.GET.get('USED')
    
    if cat_id:
        products = Product.objects.filter(categories=cat_id, status='Published')
    elif price_filter_id:
        products = Product.objects.filter(price_filter=price_filter_id, status='Published')
    elif color_id:
        products = Product.objects.filter(color=color_id, status='Published')
    elif brand_id:
        products = Product.objects.filter(brand=brand_id, status='Published')
    elif ATOZ_id:
        products = Product.objects.filter(status='Published').order_by('name')
    elif ZTOA_id:
        products = Product.objects.filter(status='Published').order_by('-name')
    elif PRICE_LOW_TO_HIGH_id:
        products = Product.objects.filter(status='Published').order_by('price')
    elif PRICE_HIGH_TO_LOW_id:
        products = Product.objects.filter(status='Published').order_by('-price')
    elif NEW_id:
        products = Product.objects.filter(status='Published', condition='New').order_by('-id')
    elif USED_id:
        products = Product.objects.filter(status='Published', condition='Used').order_by('-id')
    else:
        products = Product.objects.filter(status='Published').order_by('-id')

    brand_count = get_brand_count(request)
    # print(brand_count)
    
    context = {
        'products': products,
        'categories' : categories,
        'price_filter' : price_filter,
        'colors' : colors,
        'brands': brands,
        'brand_count' : brand_count,
    }
    
    return render(request, 'store_app/products.html', context)

def get_brand_count(request):
    brand_id = request.GET.get('brand')
    products_by_brand = Product.objects.filter(brand=brand_id, status='Published')
    value = products_by_brand.count()
    return value
     

def search(request):
    query = request.GET.get('query')
    
    products = Product.objects.filter(name__icontains=query)
    
    context = {
        'products' : products
    }
    
    return render(request, 'store_app/search.html', context)



def product_detail(request, id):
    single_product = Product.objects.filter(id=id)
    
    context = {
        'single_product' : single_product,
    }
    
    return render(request, 'store_app/single_product.html', context)
