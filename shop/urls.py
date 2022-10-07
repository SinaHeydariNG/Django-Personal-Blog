from django.urls import  path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/' , views.list , name='shop'),
    path('products/product/<slug:slug>' , views.detail , name='detail'),
    path('products/category/<slug:slug>' , views.category , name='category'),
    path('products/cart' , views.cart , name='cart'),
    path('products/add-to-cart/<int:pk>' , views.add_cart , name='add-to-cart'),
    path('products/remove-from-cart/<int:pk>' , views.remove_cart , name='remove-from-cart'),
    path('products/reduce-from-cart/<int:pk>' , views.reduce_cart , name='reduce-from-cart'),
    path('products/purchase-from-cart/<int:pk>' , views.purchase , name='purchase-from-cart'),
]