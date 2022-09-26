from django import forms
from .models import Category,Product



class CategoryModelForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = [
            "title",
            "status",
        ]



class ProductModelForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            "category",
            "title",
            "content",
            "price",
            "status",
            "cover_image",
            "is_home",
        ]