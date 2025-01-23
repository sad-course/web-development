from django import forms
from .models import Category, Supplier

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(),)
