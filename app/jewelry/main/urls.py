from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductList),
    path('products/create', ProductCreate),
    path('products/<int:pk>', ProductDetail),
    path('products/<int:pk>/delete', ProductDelete),
    path('products/<int:pk>/update', ProductUpdate),
]