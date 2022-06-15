from django.shortcuts import render
from .models import Event


def shop(request):
    posts = Event.objects.order_by()
    return render(request, 'shop/shop.html', {'posts': posts})

