from ast import List
from django.shortcuts import render, redirect
from .models import Product, Supplier, Category
from .forms import ProductForm, CategoryForm, SupplierForm
from django.views import generic

# Create your views here.
class ProductList(generic.ListView):
    queryset = Product.objects.all()
    template_name = "product/index.html"
    context_object_name = "products"

class ProductCreate(generic.CreateView):
    model = Product
    template_name = "product/create.html"
    form_class = ProductForm
    success_url = "/"

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "category/index.html"
    context_object_name = "categories"

class CategoryCreate(generic.CreateView):
    model = Category
    template_name = "category/create.html"
    form_class=CategoryForm
    success_url="/category/"
    
class SupplierList(generic.ListView):
    queryset = Supplier.objects.all()
    template_name = "supplier/index.html"
    context_object_name = "suppliers"

class SupplierCreate(generic.CreateView):
    model = Supplier
    template_name = "supplier/create.html"
    form_class=SupplierForm
    success_url="/supplier/"

def product_detail(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        context = {"product": product}
        return render(request, "product/detail.html", context=context)
    
def update_product(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
        
def delete_product(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('index')

def category_detail(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)
        context = {"category": category}
        return render(request, "category/detail.html", context=context)

def supplier_index(request):
    if request.method == 'GET':
        context = {"suppliers": Supplier.objects.all()}
        return render(request, "supplier/index.html", context=context)

def supplier_detail(request, supplier_id):
    if request.method == 'GET':
        supplier = Supplier.objects.get(id=supplier_id)
        context = {"supplier": supplier}
        return render(request, "supplier/detail.html", context=context)


