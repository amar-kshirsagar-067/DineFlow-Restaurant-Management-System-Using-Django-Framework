from django.db import models
from django.contrib.auth.models import User # this model is used for creating registration form

# Create your models here.

class Category(models.Model):
    food_names = models.CharField(max_length=200,null = False, blank = False)
    image = models.CharField(max_length=3000,null = True, blank = True)
    description = models.TextField(max_length=1000,null = False, blank = False)

    """Yes, exactly! If you do not use the __str__() method in the 'Category' model, 
    Django will display the default representation of the 'Category' instances, 
    which is the primary key (id), in places like the admin panel or when accessing the related objects through a ForeignKey."""

    def __str__(self):
        return f'{self.food_names}'
    
class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=400,null = False, blank = False)
    item_description = models.TextField(max_length=1000,null = False, blank = False)
    price = models.FloatField(null = False, blank = False)
    offer_price = models.FloatField(null = False, blank = False)
    item_image = models.URLField(default="https://t3.ftcdn.net/jpg/08/29/90/88/360_F_829908823_kYsRKdQcIaYEAhHRAZTIXuSKvuVPif8w.jpg")
    quantity = models.IntegerField(null = False, blank = False)
    underrated_item = models.BooleanField(default=False,help_text="0-show, 1-hidden")
    new_added_item = models.BooleanField(default=False, help_text="Check to show in New Arrivals")
    
    def __str__(self):
        return f'{self.name}'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)

    """
    The @property decorator is a great way to create a method that behaves like an attribute, 
    making your code cleaner. 
    In your case, you are defining a 'total_price' property that calculates the total price of an item in the cart based on its quantity and the offer_price of the product.
    """
    @property
    def total_price(self):
        return self.product_qty * self.product.offer_price

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)