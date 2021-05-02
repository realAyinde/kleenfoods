from django.urls import path
from core import views
from .views import HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.item_list, name='item_list'),
    path('shop/<slug:category_slug>/', views.item_list, name='item_list_by_category'),
    path('shop/<int:id>/<slug:slug>/', views.item_detail, name='item_detail')
]
