"""qrmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from products.views import category_create, category_delete, category_list, category_update,  product_create, product_delete, product_list, product_update,category_show
from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    #Category
    path('<slug:category_slug>', category_show, name='category_show'),
    path('manage/category_list/',category_list, name="category_list"),
    path('manage/category_create/',category_create, name="category_create"),
    path('manage/category_delete/<int:pk>/',category_delete, name="category_delete"),
    path('manage/category_update/<int:pk>/',category_update, name="category_update"),
    #Product
    path('manage/product_create/',product_create, name="product_create"),
    path('manage/product_list/',product_list, name="product_list"),
    path('manage/product_update/<int:pk>/',product_update, name="product_update"),
    path('manage/product_delete<int:pk>/',product_delete, name="product_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Burası resimleri çıkarmaya yarar settings.py kısmında da ayarı var 
