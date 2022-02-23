from itertools import product
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import Cart, Contact, Order, OrderItem, Product, Profile, Review
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User



@login_required(login_url = 'login')
def addreview(request):
    if request.method == 'POST':

        itemid = request.POST.get('productid')
        item = Product.objects.filter(pk = itemid ).first()
        
        newReview = Review()
        newReview.user = request.user
        newReview.post = item
        newReview.comment = request.POST.get('comment')
        
        newReview.save()

        
        
        
        messages.success(request, 'Commeted successfully')
    return redirect('/')