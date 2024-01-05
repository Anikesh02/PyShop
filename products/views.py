from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

#Products ->  index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})
    
def new(request):
    return HttpResponse("Hello, world. You're in new products.")
