from django.shortcuts import render, redirect
from .models import Product
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
            form.save()
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