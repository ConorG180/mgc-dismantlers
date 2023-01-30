from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, Category, Make, Model, Part
from wishlist.models import Wishlist
from .forms import Product_form
from django.db.models import Q
from .filters import ProductFilter
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User


def render_products(request):
    products = Product.objects.all()
    # print(f"FIRST RENDERING {products}")
    if request.method == "GET":
        product_filter = ProductFilter(request.GET, queryset=products)
        # print(f"Here is the filter{dir(product_filter)}")
        products = product_filter.qs
        context = {
            "products": products,
            "product_filter": product_filter
        }
    # print(f"SECOND RENDERING {products} ")
    return render(request, 'products/products.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect(reverse('products'))


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    make = product.car_model.make
    product_form = Product_form(request.POST, request.FILES, instance=product,)
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
    product_form = Product_form(request.POST or None, request.FILES)
    if request.method == "POST":
        if product_form.is_valid():
            product = product_form.instance
            product_form.save()
            # Send email to users who have item added to wishlist

            # Get items on wishlist which only wish to be contacted
            # When item is added, relevant make/model, and year == 
            # to chosen year or 0 (Which means all years) and part ==
            # to chosen year or 0 (Which means all parts).
            wishlist_entries = Wishlist.objects.filter(Q(on_add=True) & Q(make_id=product.make_id) & Q(car_model_id=product.car_model_id) & (Q(model_year=product.model_year_id) | Q(model_year=0)) & (Q(part_id=product.part_id) | Q(part_id=0)))
            # Only do something if wishlist isn't empty
            if wishlist_entries.count():
                # Iterate over every wishlist entry
                for wishlist_entry in wishlist_entries:
                    # put all user emails into emails list
                    emails = [user.email for user in wishlist_entry.user.all()]

                # Create email subject
                subject = render_to_string(
                    'products/wishlist-emails/wishlist_item_added_subject.txt',
                    {'product': product}
                )
                # Create email body
                body = render_to_string(
                    'products/wishlist-emails/wishlist_item_added_body.txt',
                    {'product': product}
                )
                # Send emails to emails on wishlist.
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    emails
                )
                print("EMAIL(S) SHOULD BE SENT")
            print("Wishlist empty, no emails sent")
            return redirect(reverse('products'))
        else:
            print(product_form.errors)
            print("form not valid!!!!!!!!")
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
    context = {
        "category": cat,
        "products": categorized_products
    }
    return render(request, "products/products.html", context)


def load_models(request):
    # make = request.GET.get('make')
    make = get_object_or_404(Make, name=request.GET.get("make"))
    models = Model.objects.filter(make=make).order_by("car_model")
    return render(request, 'products/model_dropdown_list_options.html', {'models': models})
