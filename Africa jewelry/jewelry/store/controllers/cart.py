from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import Cart, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def addtocart(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            
            product_check = Product.objects.get(id = prod_id )
            
            
            if(product_check):
                
                if(Cart.objects.filter(user=request.user.id, product= prod_id ) ):
                    return JsonResponse({'status': "Product Already in Cart"  } )
                else:
                    
                    prod_qty =  request.POST.get('product_qty' )
                    qty = int(prod_qty)
                    check = int(product_check.quantity)
                    
                    

                    if check >= qty:
                        user= str(request.user)
                        product = str(prod_id)
                        product_qty=str(prod_qty)
                        
                        Cart.objects.create(user= request.user,product =Product.objects.get(pk=prod_id)  ,product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully"  })
                        
                    else:
                        return JsonResponse({'status': "Only" + str(product_check.quantity) +" quantity available" })


            else:
                return JsonResponse({'status': "No such product found"  } )

        else:
            return JsonResponse({'status': "Login to continue"  } )
        
    return redirect('/')

@login_required(login_url = 'login')
def cart(request):
    userprofile = User.objects.filter(id = request.user.id).first()
    cart = Cart.objects.filter(user=request.user)

    paginator = Paginator(cart, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'cart':cart,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        }
    
    return render(request,"store/cart.html",context)

@login_required(login_url = 'login')
def updatecart(request):
    if request.method == 'POST':
        prod_id =request.POST.get('product_id') 
       
        
        if(Cart.objects.filter(user = request.user,product = prod_id)):
            prod_qty =  request.POST.get('product_qty' )
            cart = Cart.objects.get(product= prod_id,user = request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated Successfully " } )
    return redirect('/')

@login_required(login_url = 'login')          
def deletecartItem(request):
    if request.method == 'POST':
        prod_id =request.POST.get('product_id') 
        
        
        
        if(Cart.objects.filter(user = request.user,product = prod_id)):
            cart = Cart.objects.get(product= prod_id,user = request.user)
            
            cart.delete()
            return JsonResponse({'status': "Deleted Successfully " } )
            
            
    
        
    return redirect('/')
