from django.contrib import admin

from products.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=(
        "pk",
        "title",
        "slug",
        "status",
        "updated_at",
    )
    list_filter=(
        "status",
        
    )

    list_editable=(
        "status",
        "title",
    )

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=(
        "pk",
        "title",
        "price",
        'cover_image',
        "slug",
        "status",
        "updated_at",
    )
    list_filter=(
        "status",

    )
    list_editable=(
        "status",
        "title",
    )

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)