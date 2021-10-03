from django.conf.urls import url
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('products/<int:pk>/delete', ProductDelete.as_view()),
    path('products/<int:pk>/update', ProductUpdate.as_view()),
    # path('products/<int:pk>/buy', product_buy),
    path('register_firm', firm_create),
    path('register_buyer', buyer_reg),
    # path('update/buyer', buyer_update),
    path('login', user_login),
    path('logout', user_logout),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
