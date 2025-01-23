from django.urls import path
from .views import index, product_detail, update_product, delete_product, create_product

urlpatterns = [ 
    path("", index, name='index'),
    path("<int:product_id>/", product_detail, name='product_detail'),
    path("create/", create_product, name='create_product'),
    path("<int:product_id>/update/", update_product, name='update_product'),
    path("<int:product_id>/delete/", delete_product, name='delete_product'), 
]