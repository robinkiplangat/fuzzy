from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name="product-list"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),
    # url(r'^search/', views.search, name='search'),
    url(r'^products_search/', views.ProductSearch.as_view(), name="product-search"),
    ]
