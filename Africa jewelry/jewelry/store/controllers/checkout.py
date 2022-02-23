from itertools import product
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import Cart, Order, OrderItem, Product, Profile
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User

@login_required(login_url = 'login')
def index(request):
    fromCart = Cart.objects.filter(user = request.user)
    for item in fromCart:
        if item.product_qty > item.product.quantity:
            
            Cart.objects.filter(pk=item.pk).delete()
            
    cartItem = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cartItem:
        total_price = total_price + item.product.selling_price * item.product_qty
    
    userprofile = Profile.objects.filter(user = request.user).first



    context = {
        'cartItem':cartItem,
        'total_price':total_price,
        'userprofile':userprofile,
        'a': Cart.objects.all(),
    }
    return render(request,"store/checkout.html",context)

@login_required(login_url = 'login')
def placeorder(request):
    
    if request.method == 'POST':
        
        userprofile = User.objects.filter(id = request.user.id).first()

        if not userprofile.first_name:
            userprofile.first_name = request.POST.get('fname')
            userprofile.last_name = request.POST.get('lname')
            userprofile.save()
        if not Profile.objects.filter(user = request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phoneno')
            userprofile.street_address = request.POST.get('streetaddress')
            userprofile.city = request.POST.get('city')
            userprofile.save()



        newOrder = Order()
        newOrder.user = request.user
        newOrder.fname = request.POST.get('fname')
        newOrder.lname = request.POST.get('lname')
        newOrder.email = request.POST.get('email')
        newOrder.phone_no = request.POST.get('phoneno')
        newOrder.street_address = request.POST.get('streetaddress')
        newOrder.city = request.POST.get('city')
        newOrder.order_notes = request.POST.get('ordernotes')
        cart = Cart.objects.filter(user = request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        newOrder.total_price = cart_total_price
        trackNo = 'Africa' + str(random.randint(11111111,99999999))
        while Order.objects.filter(traking_no = trackNo) is None:
            trackNo = 'Africa' + str(random.randint(11111111,99999999))

        newOrder.traking_no = trackNo
        newOrder.save()

        newOrderitems =Cart.objects.filter(user = request.user)
        for ordItem in newOrderitems:
            OrderItem.objects.create(
                order = newOrder,
                product = ordItem.product,
                price = ordItem.product.selling_price,
                quantity = ordItem.product_qty,

            )

            #
            orderProduct = Product.objects.filter(id = ordItem.product_id).first()
            orderProduct.quantity = orderProduct.quantity - ordItem.product_qty
            orderProduct.save()
        #
        Cart.objects.filter(user = request.user).delete()

        messages.success(request, 'Your Order has been placed successfully')
    return redirect('/')