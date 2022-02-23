from itertools import product
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import Cart, Contact, Order, OrderItem, Product, Profile
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User



@login_required(login_url = 'login')
def addcontact(request):
    if request.method == 'POST':
        
        userprofile = User.objects.filter(id = request.user.id).first()

        if not userprofile.first_name:
            userprofile.first_name = request.POST.get('fname')
            userprofile.last_name = request.POST.get('lname')
            userprofile.save()



        newOrder = Contact()
        newOrder.user = request.user
        newOrder.subject = request.POST.get('subject')
        newOrder.message = request.POST.get('message')
        
        newOrder.save()

        
        
        
        messages.success(request, 'Send successfully')
    return redirect('/')