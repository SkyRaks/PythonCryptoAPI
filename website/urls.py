from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('purchase_coin/<str:coin>/', views.purchase_coin, name='purchase_coin'),
]