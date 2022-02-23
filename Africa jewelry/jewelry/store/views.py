
from multiprocessing import context
from sre_parse import State
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    context = {
        
    }
    return render(request, 'store/index.html',context)
def shop(request):
    Item_list = Product.objects.exclude(quantity = 0)

    paginator = Paginator(Item_list, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'blogs': Event.objects.all()[:4],
        'discount': DiscountEvent.objects.all()[:4],
        
    }
    return render(request, 'store/product/shop.html',context)
def blog(request):
    context = {
        'blogs': Event.objects.all(),
        'discount': DiscountEvent.objects.all(),
        'item': Product.objects.all()[:4]
    }
    return render(request, 'store/Blog/blog.html',context)
# def search(request):
#     Item_list = Product.objects.all()
#     query = request.GET.get('q')
#     if query:
#         Item_list = Item_list.filter(
#             Q(name__icontains=query) |
#             Q(small_description__icontains=query) |
#             Q(description__icontains=query)
#         ).distinct()

#     paginator = Paginator(Item_list, 3)
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
   

#     try:
#         paginated_queryset = paginator.page(page)
#     except PageNotAnInteger:
#         paginated_queryset = paginator.page(1)
#     except EmptyPage:
#         paginated_queryset = paginator.page(paginator.num_pages)

    
    
#     context = {
        
#         'queryset': paginated_queryset,
#         'page_request_var': page_request_var,
        
#     }

#     return render(request, 'store/product/shop.html',context)

def search(request):
    if request.method == 'POST':
        searched = request.POST.get('q')
        if searched == '':
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            products = Product.objects.filter(name__contains=searched).first()

            if products:
                return redirect('detail/'+ str(products.id) +'/'+products.category.name)
            else:
                messages.info(request,'No Product matched your search')
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
def searchproduct(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productList = list(products)

    return JsonResponse(productList,safe = False)
def detail(request, pk,pro_cate):
    
    if(Category.objects.filter(name=pro_cate,status = 0)):
        if(Product.objects.filter(pk=pk,status = 0)):
            ItemDetail= Product.objects.filter(pk=pk,status = 0).first()
            rev = Review.objects.filter(post = ItemDetail)
            context = {'ItemDetail':ItemDetail,
            'review':rev,
            
            }

        else:
            messages.error(request, "No such category found" )
            return redirect('shop')
    else:
        messages.error(request, "No such category found" )
        return redirect('shop')

    
    
    return render(request, 'store/product/product-detail.html',context)

@login_required(login_url = 'login')
def account(request):
    order = Order.objects.filter(user = request.user)

    context = {
        'order':order,
    }
    return render(request, 'store/account.html',context)

@login_required(login_url = 'login')
def contactus(request):
    userprofile = Profile.objects.filter(user = request.user).first
    context = {
        'userprofile':userprofile,
    }
    return render(request,'store/contactus.html',context)