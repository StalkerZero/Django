from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import *

from .forms import *
from .models import Product, Sold


class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'sort', 'price', 'quantity']
    template_name = 'product/create.html'

    def form_valid(self, form):
        product = Product()
        product.title = form.data['title']
        product.sort = form.data['sort']
        if int(form.data['quantity']) <= 0:
            return HttpResponseRedirect("/products/create")
        if float(form.data['price']) <= 0.00:
            return HttpResponseRedirect("/products/create")
        product.price = form.data['price']
        product.quantity = form.data['quantity']
        product.id_firm = self.request.user.firm
        product.save()
        return HttpResponseRedirect("/products")


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def post(self, request, *args, **kwargs):
        form = TestForm(request.POST)
        p = Product.objects.get(pk=form.data['id'])
        if p.quantity < int(form.data['quantity']):
            return HttpResponseRedirect("/products")
        p.quantity -= int(form.data['quantity'])
        p.save()
        sold = Sold()
        sold.id_product = p
        sold.id_buyer = request.user.buyer
        sold.quantity = int(form.data['quantity'])
        if request.user.buyer.buyer_type == 2:
            sold.buyer_type = "Юр. лицо"
        else:
            sold.buyer_type = "Частный"
        sold.save()
        return HttpResponseRedirect("/products")


class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'sort', 'price', 'quantity']
    template_name = 'product/update.html'
    success_url = '/products'


# def product(request, pk):
#     p = Product.objects.get(pk=pk)
#     return render(request, "product/buy.html", {'form': p})
#
#
# def product_buy(request, pk):
#     product(request, pk)
#     if request.method == "POST":
#         p = Product.objects.get(pk=pk)
#         p.quantity -= request.POST.quantity
#         p.save()
#         sold = Sold()
#         sold.id_product = pk
#         sold.id_buyer = request.user.buyer
#         sold.quantity = request.POST.quantity
#         sold.buyer_type = request.user.buyer.buyer_type
#         sold.save()
#         return HttpResponseRedirect("/products")


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = '/products'


def firm_create(request):
    form = FirmCreate(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, "firm/create.html", {'form': form})


def buyer_reg(request):
    form = BuyerCreate(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, "buyer/create.html", {'form': form})


# def buyer_update(request):
#     form = BuyerUpdate(request.POST or None)
#     if form.is_valid():
#         user = form.save()
#         login(request, user)
#         return HttpResponse("Удачно")
#     return render(request, "buyer/update.html", {'form': form})


def user_login(request):
    form = AuthenticationForm(data=(request.POST or None))
    if form.is_valid():
        login(request, form.get_user())
        return redirect('/')
    return render(request, "login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')
