from email.policy import default
from random import choices
from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models
from matplotlib.pyplot import title
from sqlalchemy import true

DEFAULT_STATUS="draft"
STATUS=[
    ("draft","Taslak"),
    ('published',"Yayinlandi"),
    ('deleted','Silindi')
]


class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(
        max_length=200,
        default="",
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        
    )
    title=models.CharField(max_length=200)
    slug=models.SlugField(
        default="",
        max_length=200
        

    )
    cover_image=models.ImageField(
        upload_to="media",
        null=True,
        blank=True,

    )
    content=models.TextField(max_length=200) 
    price=models.FloatField()
    is_home = models.BooleanField(default=False)
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title