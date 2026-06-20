from django.urls import path
from .views import home, product_detail, category_products, search_products

urlpatterns = [
    
    path('', home, name='home'),
    path('product/<int:product_id>/',product_detail,name='product_detail'),
    path('category/<int:category_id>/',category_products,name='category_products'),
    path('search/',search_products,name='search_products'),

]
