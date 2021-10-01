from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import *

from .forms import FirmCreate
from .models import Product, Firm


class ProductCreate(CreateView):
    model = Product
    fields = ['Название', 'Сорт', 'Цена', 'Количество']
    template_name = 'product_create.html'
    success_url = '/products'

    def foreign(self):
        Product.id_firm = self.request.user_id


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'sort', 'price', 'quantity']
    template_name = 'product_update.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = '/products'


def firm_create(request):
    form = FirmCreate(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "firm_create.html", {'form': form})
