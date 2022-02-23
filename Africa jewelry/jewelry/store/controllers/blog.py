
from django.shortcuts import render
from store.models import DiscountEvent, Event


def discount(requast,pk):
    events = DiscountEvent.objects.filter(pk = pk).first()
    recent = DiscountEvent.objects.all()[:3]
    context = {
         'events':events,
         'recent':recent
    }
    return render(requast, 'store/Blog/view.html',context)

def post(requast,pk):
    events = Event.objects.filter(pk = pk).first()
    recent = DiscountEvent.objects.all()[:3]
    context = {
         'events':events,
         'recent':recent
    }
    return render(requast, 'store/Blog/view.html',context)