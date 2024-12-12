from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=250,unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

