from django.urls import path, include, re_path as url
from stock.views import *

urlpatterns = [
    url('products/', stock_products, name="stock_products"),
    url('', home, name="home"),
]
