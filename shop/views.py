from pydoc import pager
import django
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect
from .models import (Products , Category , OrderList , OrderProduct , Orders)
from main.models import SiteInfo
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


def list(request):
    information = SiteInfo.objects.last()
    if request.method == "POST":
        if request.POST['title']:
            title = request.POST['title']
            print(title)
            prodcuts = Products.objects.filter(title__icontains = title)
    else:    
        prodcuts = Products.objects.all()
    paginator = Paginator(prodcuts , 3)
    page_url = request.GET.get('page')
    prodcuts = paginator.get_page(page_url)
    categories = Category.objects.all()
    context = {
        "categories" : categories,
        "products" : prodcuts,
        "information" : information}

    return render(request , 'shop/list.html' , context)    

def detail(request , slug):
    information = SiteInfo.objects.last()
    prodcuts = Products.objects.filter(category__slug = slug)
    product = Products.objects.get(slug=slug)
    paginator = Paginator(prodcuts , 3)
    page_url = request.GET.get('page')
    prodcuts = paginator.get_page(page_url)
    categories = Category.objects.all()
    context = {
        "product" : product,
        "categories" : categories,
        "products" : prodcuts,
        "information" : information}

    return render(request , 'shop/detail.html' , context)   

def category(request , slug):
    information = SiteInfo.objects.last()
    prodcuts = Products.objects.filter(category__slug = slug)
    paginator = Paginator(prodcuts , 3)
    page_url = request.GET.get('page')
    prodcuts = paginator.get_page(page_url)
    categories = Category.objects.all()
    context = {
        "categories" : categories,
        "products" : prodcuts,
        "information" : information}

    return render(request , 'shop/list.html' , context)   

@login_required
def cart(request):
    information = SiteInfo.objects.last()
    user = request.user
    ordered = OrderList.objects.get(user = user)
    shiffting = 20.00
    latest_price = ordered.get_final_price() + shiffting
    context = {
        "latest_price" : latest_price,
        "information" : information,
        "ordered" : ordered}
    return render(request , 'shop/cart.html' , context)

def add_cart(request , pk):
    product = get_object_or_404(Products , pk=pk)
    slug = product.slug
    print(slug)
    order_product , created = OrderProduct.objects.get_or_create(
        product = product,
        user = request.user,
        ordered = False,
    )
    order_qs = OrderList.objects.filter(user = request.user , ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk = product.pk).exists():
            order_product.quantity += 1
            order_product.save()
            return redirect("shop:detail" , slug=slug)
        else:
            order.products.add(order_product)
            return redirect("shop:detail" , slug=slug)
    else:
        date_ordered = datetime.now()
        order = OrderList.objects.create(user = request.user , date_ordered = date_ordered)
        order.products.add(order_product)

        return redirect("shop:cart" , slug=slug)


def remove_cart(request , pk):
    product = Products.objects.get(pk=pk)
    slug = product.slug
    user = request.user
    ordered_qs = OrderList.objects.filter(user = user , ordered = False)
    if ordered_qs.exists():
        order = ordered_qs[0]
        if order.products.filter(product__pk = product.pk):
            order_product = OrderProduct.objects.filter(
                user = request.user,
                ordered = False,
                product = product
            )
            order_product.delete()
            return redirect("shop:detail" , slug=slug)
        else:
            return redirect("shop:detail" , slug=slug)    
    else:
        return redirect("shop:detail" , slug=slug)         

def reduce_cart(request , pk):
    product = Products.objects.get(pk=pk)
    slug = product.slug
    user = request.user
    ordered_qs = OrderList.objects.filter(user = user , ordered = False)
    if ordered_qs.exists():
        order = ordered_qs[0]
        if order.products.filter(product__pk = product.pk).exists():
            order_product = OrderProduct.objects.filter(
                user = user,
                ordered = False,
                product = product,
            ).last()
            print(order_product.quantity)

            if order_product.quantity > 1:
                order_product.quantity=order_product.quantity - 1
                order_product.save()
                return redirect("shop:detail" , slug=slug)
            else:
                order_product.delete()
                return redirect("shop:detail" , slug=slug)
        else:
            return redirect("shop:detail" , slug=slug)    
    else:
        return redirect("shop:detail" , slug=slug)         

@login_required
def purchase(request , pk):
    if request.method == "POST":
        order = OrderList.objects.get(pk = pk)
        submitted_order = Orders.objects.create(
            user = request.user,
            products = order,
            date = datetime.now(),
            address = request.POST['address'],
            reciever = request.POST['reciever'],
        )
        print(order.ordered)
        order.save()
        submitted_order.save()
        return HttpResponse("Thanks for trusting and purchasing!!!")
