from django.urls import path
from . import views

app_name = "store_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all_products, name='products'),
    path('products/product/<str:id>/', views.product_detail, name='product-detail'),
    
    path('search/', views.search, name='search'),
]