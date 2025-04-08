from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('index/',views.Index,name= 'home' ),
   path('shop/', views.Shop, name="shop"),
   path('product-single/', views.Product_Single, name= 'product-single'),
   path('shop-sider/',views.Shope_Sider, name= "s-sider"),
    path('shop-sider/',views.Shope_Sider, name= "s-sider"),
     path('cart/',views.Cart, name= "cart"),
      path('checkout/',views.Checkout, name= "checkout"),
       path('confirm/',views.Confirm, name= "confirm"),
        path('pricing/',views.Pricing, name= "price"),
         path('comment-section/<int:id>',views.comments, name= "comment"),

]
