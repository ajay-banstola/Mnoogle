from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

app_name = 'account'

urlpatterns = [
    path('custreg/', views.custreg, name='custreg'),
    path('products/', views.products, name='products'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_product', views.add_product, name='add_products'),
    path('message', views.message, name='sent'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/user_info/', views.user_info,name='edit_info'),
    path('profile/user_info/password/', views.change_password, name='change_password'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
]
