from django.shortcuts import render, redirect
from .models import Product, Supplier, Category
from .forms import ProductForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {"products": Product.objects.all()}
        return render(request, "product/index.html", context=context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            categories = form.cleaned_data['categories']
            supplier = form.cleaned_data['supplier']

            product = Product(name=product_name, code=code, description=description, price=price, quantity=quantity, supplier=supplier)
            product.save()
            product.categories.set(categories)


            return redirect('index')
    else:
        form = ProductForm()
    return render(request, "product/create.html", {"form": form})

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
    
def category_index(request):
    if request.method == 'GET':
        context = {"categories": Category.objects.all()}
        return render(request, "category/index.html", context=context)

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
