from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, Category, Make, Model, Part
from .forms import Product_form
from django.db.models import Q


def render_products(request):
    products = Product.objects.all()
    print(products)
    context = {
        "products": products
    }
    return render(request, 'products/products.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    print(product)
    product.delete()
    return redirect(reverse('products'))


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    make = product.car_model.make
    product_form = Product_form(request.POST, instance=product)
    if request.method == "POST":
        if product_form.is_valid():
            product_form.save()
            return redirect(reverse('products'))
    else:
        product_form = Product_form(instance=product)
        context = {
            "product_form": product_form,
            "product": product
        }
        return render(request, "products/edit-product.html", context)


def add_product(request):
    if request.method == "POST":
        product_form = Product_form(request.POST)
        if product_form.is_valid():
            print("We'gre getting here 44")
            product_form.save()
            print("We'gre getting here 46")
            return redirect(reverse('products'))
        else:
            print(product_form.errors)
            return redirect(reverse('add_product'))
    else:
        product_form = Product_form()
        context = {
            "product_form": product_form,
        }
        return render(request, "products/add-product.html", context)


def search_product(request):
    products = Product.objects.all()
    if request.method == "GET":
        user_search_query = request.GET["user_search_query"]
        if not user_search_query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))
        queries = Q(color__icontains=user_search_query) | Q(car_model__car_model__icontains=user_search_query) | Q(car_model__make__name__icontains=user_search_query) | Q(part__name__icontains=user_search_query)
        products = products.filter(queries)
        context = {
            "user_search_query": user_search_query,
            "products": products,
            "products_count": products.count()
        }
        return render(request, 'products/search.html', context)
    return render(request, 'products/search.html', {})


def categorize_products(request, cat):
    categorized_products = Product.objects.filter(part__category__friendly_name=cat)
    # category = Category.objects.get(friendly_name=)
    # print("variable")
    print(categorized_products)
    # print("category object")
    # print(category)
    context = {
        "category": cat,
        "products": categorized_products
    }
    return render(request, "products/products.html", context)


def load_models(request):
    make = request.GET.get('make')
    make_id = Make.objects.get(name=make).id
    models = Model.objects.filter(make_id=make_id).all()
    return render(request, 'products/model_dropdown_list_options.html', {'models': models})
