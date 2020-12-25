"""ShoeShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import homes, admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homes.category),
    path('product/<int:product_id>/', homes.detail),
    path('category/', homes.category),
    path('cart/', homes.cart),
    path('cart/add/<int:shoe_id>/', homes.category_add),
    path('cart/update/', homes.card_update),
    path('cart/checkout/', homes.checkout),
    path('login/', homes.login),
    path('logout/', homes.logout),
    path('register/', homes.register),
    path('product/', homes.detail),
    path('dashboard/', admins.current_datetime)
]
