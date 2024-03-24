from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('view-coupon', ViewStore, name='view-coupon'),
    path('login', Loginview.as_view(), name='login'),
    path('search-results', search_results, name='search-results'),
    path('checkout/<code>', coupon_checkout, name='checkout'),
    path('logout', Logoutview, name='logout'),
]
