from django import forms

import products
from products.models import Product


class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

