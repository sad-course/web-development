from django import forms
from .models import Category, Supplier
import re

class DatePicker(forms.Widget):
    def render(self, name, value, attrs=None):
        if value is not None:
            value = value.strftime('%Y-%m-%d')
        return super().render(name, value, attrs)
    
    
class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 5 characters long.")
        return name
        
    def clean_code(self):
        code = self.cleaned_data['code']
        if not re.match(r"^([\w]|[\d])+$", code):   
            raise forms.ValidationError("Code must contains only letters and numbers.")
        return code

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class SupplierForm(forms.Form):
    name = forms.CharField(max_length=250)
    cep = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    