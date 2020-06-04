from django.urls import path
# from .import views
from. views import ProductList,ProductUpdate, ProductCreate, ProductDelete, Homepage
urlpatterns = [
    path('',Homepage.as_view()),
    path('list/',ProductList.as_view()),
    path('list/product_update/<pk>',ProductUpdate.as_view()),
    path('product_create/',ProductCreate.as_view()),
    path('list/d<pk>/',ProductDelete.as_view())
]