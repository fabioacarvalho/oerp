from django.shortcuts import render

# Create your views here.


def stock_products(request):
    return render()


def home(request):
    return render(request, 'base.html', locals())