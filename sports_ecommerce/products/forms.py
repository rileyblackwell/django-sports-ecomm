from django import forms
from django.forms.fields import CharField, DecimalField

from .models import Product


class ProductForm(forms.ModelForm):
	product_name = forms.CharField(widget=forms.TextInput(
		attrs={
					 		
	}))
	color = forms.CharField(widget=forms.TextInput(
		attrs={
					 		
	}))
	size = forms.CharField(widget=forms.TextInput(
		attrs={
			'placeholder': 'M',
			'size': '2'		 		
	}))
	brand = forms.CharField(widget=forms.TextInput(
		attrs={
					 		
	}))
	price = forms.DecimalField()
	
	class Meta:
		model = Product
		fields = [
			'product_name',
        	'color',
        	'size',
			'brand',
        	'price'
		]