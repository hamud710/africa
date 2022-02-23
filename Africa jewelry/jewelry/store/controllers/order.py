
from django.shortcuts import render


from store.models import Order, OrderItem


def vieworder(requast,t_no):
    order = Order.objects.filter(traking_no = t_no).filter(user = requast.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {
         'order':order,
         'orderitems': orderitems,
    }
    return render(requast, 'store/order/view.html',context)
