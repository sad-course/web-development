from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=250)
    cep = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=250,unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Category)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name