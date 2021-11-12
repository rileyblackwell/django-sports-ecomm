from django.db import models
from django.db.models.fields import CharField, DecimalField

# Create your models here.

class Product(models.Model):
        product_name = CharField(max_length=50)
        color = CharField(max_length=25)
        size = CharField(max_length=2)
        brand = CharField(max_length=50)
        price = DecimalField(max_digits=10, decimal_places=2)
     
      

 
     