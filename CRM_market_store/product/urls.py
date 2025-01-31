from django.urls import path
from .views import (index, product_detail, update_product, 
                    delete_product, product_create, category_index,category_detail,
                    supplier_index, supplier_detail, supplier_create, category_create,
                    ProductList, CategoryList, SupplierList, ProductCreate, CategoryCreate, SupplierCreate)

urlpatterns = [ 
    path("", ProductList.as_view(), name='index'),
    path("<int:product_id>/", product_detail, name='product_detail'),
    path("create/", ProductCreate.as_view(), name='product_create'),
    path("<int:product_id>/update/", update_product, name='update_product'),
    path("<int:product_id>/delete/", delete_product, name='delete_product'), 

    path("category/",CategoryList.as_view(), name='category_index'),
    path("category/create/",CategoryCreate.as_view(), name='category_create'),
    path("category/<int:category_id>/",category_detail, name='category_detail'),


    path("supplier/",SupplierList.as_view(), name='supplier_index'),
    path("supplier/create/",SupplierCreate.as_view(), name='supplier_create'),
    path("supplier/<int:supplier_id>/",supplier_detail, name='supplier_detail')
]