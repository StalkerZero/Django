from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('products/<int:pk>/delete', ProductDelete.as_view()),
    path('products/<int:pk>/update', ProductUpdate.as_view()),
    path('firm/register', firm_create),
]
