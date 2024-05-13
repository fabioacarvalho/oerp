from django.db import models
from stock.choices import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name="Name")

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
    

class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name="Name")
    category = models.ForeignKey('stock.Category', verbose_name="Category", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="Price", null=True, blank=True)
    qtde = models.FloatField(verbose_name="Qtde", default=float(0))
    unity = models.CharField(max_length=10, verbose_name="Unity", choices=UNITY_CHOICES, default="un")

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"