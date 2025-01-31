from django import forms
from .models import Category, Product, Supplier
import re

class DatePicker(forms.Widget):
    def render(self, name, value, attrs=None):
        if value is not None:
            value = value.strftime('%Y-%m-%d')
        return super().render(name, value, attrs)
    
    
class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)
    code = forms.CharField(label="Código",max_length=250)
    description = forms.CharField(label="Descrição",widget=forms.Textarea)
    price = forms.DecimalField(label="Preço",max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(label="Quantidade")
    categories = forms.ModelMultipleChoiceField(label="Categorias",queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,)
    supplier = forms.ModelChoiceField(label="Fornecedor",queryset=Supplier.objects.all(),)

    class Meta:
        model=Product
        fields = ["name","code","price","description","quantity","categories","supplier",]

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if not quantity >= 0:
            raise forms.ValidationError("Quantidade deverá ser maior ou igual a zero.")
        return quantity

    def clean_price(self):
        price = self.cleaned_data['price']
        print(price)
        if price <= 0:
            raise forms.ValidationError("Preço deve ser maior que zero.")
        return price

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Nome deve ter no mínimo 3 caracteres.")
        return name
        
    def clean_code(self):
        code = self.cleaned_data['code']
        if not re.match(r"^([\w]|[\d])+$", code):   
            raise forms.ValidationError("Código deverá conter somente letras e números.")
        return code

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model=Category
        fields=["name","description"]


class SupplierForm(forms.ModelForm):
    name = forms.CharField(max_length=250)
    cep = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)

    class Meta:
        model=Supplier
        fields=["name","cep","phone"]
