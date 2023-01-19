from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Make, Model, Part
from .forms import Product_form


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


def load_models(request):
    make = request.GET.get('make')
    make_id = Make.objects.get(name=make).id
    models = Model.objects.filter(make_id=make_id).all()
    return render(request, 'products/model_dropdown_list_options.html', {'models': models})
