from django.db import models

# Create your models here.





class Brand(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name=models.CharField(max_length=100)
    qty = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category=models.ManyToManyField(Category)

    class Meta:
        ordering = ["qty"]

    def __str__(self):
        return self.name


class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
        
