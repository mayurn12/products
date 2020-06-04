from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Product

# Create your views here.
class Homepage(TemplateView):
    template_name = 'product/home.html'

class ProductCreate(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    fields = ['name','weight','price']
    success_url = '/'

class ProductList(ListView): 
    template_name= 'product/post_list.html'
    model = Product

class ProductUpdate(UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    fields = ['name','weight','price']
    success_url = '/'

class ProductDelete(DeleteView):
    template_name = 'product/pdelete.html'
    model = Product
    success_url = '/'
