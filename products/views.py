from contextvars import Context
from gc import get_objects
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.utils.text import slugify
from matplotlib.pyplot import get
from matplotlib.style import context
from products.forms import CategoryModelForm, ProductModelForm
from products.models import STATUS, Category, Product

def index(request):
    context = dict()

    products = Product.objects.filter(
        status = "published",#Burası status olursa yazdırılmaz published olması lazım çünkü burası filter kısmı olması gerekenleri eklediğimiz kısım 
        is_home=True,
    ).exclude(cover_image='')

    context['products'] = products
    return render(request,"index.html",context)





#CATEGORY

def category_show(request,category_slug):
    context = dict()
    context["category"]  = get_object_or_404(Category,slug=category_slug)
    context["items"]  = Product.objects.filter(
        category=context['category'],
        status="published",
    )
    return render(request,"product/category_show.html",context)

def category_list(request):
    context=dict()
    context["items"] = Category.objects.all().order_by("-pk")
    return render(request,"manage/category_list.html",context)

def category_create(request):
    context=dict()
    context["title"] = "Ürün Grubu Oluşturma"
    context["form"] =CategoryModelForm
    if request.method == "POST":
        print(request.POST)
        (request.FILES.get("cover_image"))
        form = CategoryModelForm(request.POST,request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Grubu Başarıyla Eklendi ")
            
    return render(request,"manage/form.html",context)

def category_update(request,pk):
    context=dict()
    item = Category.objects.get(pk=pk)
    context["title"] = f"{item.title}-pk:{item.pk} Kategori Güncelleme Formu"
    context["form"] = CategoryModelForm(instance=item)
    if request.method == "POST":
        form = CategoryModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Kategori Başarıyla Güncellendi ")
            return redirect("category_list")
            

    return render(request,"manage/form.html",context)

def category_delete(request,pk):
    item = Category.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect("category_list")

#PRODUCT

def product_list(request):
    context=dict()
    context["product"] = Product.objects.all().order_by("-pk")
    return render(request,"manage/product_list.html",context)

def product_create(request):
    context=dict()
    context["title"] = "Ürün Oluşturma"
    context["form"] =ProductModelForm
    if request.method == "POST":
        print(request.POST)
        (request.FILES.get("cover_image"))
        form = ProductModelForm(request.POST,request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Başarıyla Eklendi ")
            
      
    return render(request,"manage/form.html",context)


def product_update(request,pk):
    context=dict()
    item = Product.objects.get(pk=pk)
    context["title"] = f"{item.title}-pk:{item.pk} Ürün Güncelleme Formu"
    context["form"] = ProductModelForm(instance=item)
    if request.method == "POST":
        form = ProductModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Başarıyla Güncellendi ")
            return redirect("product_list")

    return render(request,"manage/form.html",context)

def product_delete(request,pk):
    item = Product.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect("product_list")


