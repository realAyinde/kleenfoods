from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),

    path('add/', views.ajax_cart_add, name='ajax_cart_add'),
    path('remove/', views.ajax_cart_remove, name='ajax_cart_remove'),
]
