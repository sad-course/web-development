from django.urls import path
from .views import (index, product_detail, update_product, 
                    delete_product, product_create, category_index,category_detail,
                    supplier_index, supplier_detail, supplier_create, category_create)

urlpatterns = [ 
    path("", index, name='index'),
    path("<int:product_id>/", product_detail, name='product_detail'),
    path("create/", product_create, name='product_create'),
    path("<int:product_id>/update/", update_product, name='update_product'),
    path("<int:product_id>/delete/", delete_product, name='delete_product'), 

    path("category/",category_index, name='category_index'),
    path("category/create/",category_create, name='category_create'),
    path("category/<int:category_id>/",category_detail, name='category_detail'),


    path("supplier/",supplier_index, name='supplier_index'),
    path("supplier/create/",supplier_create, name='supplier_create'),
    path("supplier/<int:supplier_id>/",supplier_detail, name='supplier_detail')
]