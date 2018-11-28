from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}     # set up a basic validator, in case I need to add any in the future.
        return errors

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Product: {self.id} {self.name} {self.price}>"
    
    objects = ProductManager()