from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Products ->  index
def index(request):
    return HttpResponse("Hello, world. You're at the products index.")
    
def new(request):
    return HttpResponse("Hello, world. You're in new products.")
