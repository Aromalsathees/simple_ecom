from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories
    }

    return render(
        request,
        "store/home.html",
        context
    )



def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    context = {
        "product": product
    }

    return render(
        request,
        "store/product_detail.html",
        context
    )


def category_products(request, category_id):

    category = get_object_or_404(
        Category,
        id=category_id
    )

    products = Product.objects.filter(
        category=category
    )

    context = {
        "category": category,
        "products": products
    }

    return render(
        request,
        "store/category_products.html",
        context
    )


def search_products(request):

    query = request.GET.get('q')

    products = Product.objects.filter(
        name__icontains=query
    )

    context = {
        "products": products,
        "query": query
    }

    return render(
        request,
        "store/search.html",
        context
    )