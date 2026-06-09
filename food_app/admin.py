from django.contrib import admin
from .models import Category, Items, Cart, Favourite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('food_names', 'description')

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'offer_price', 'quantity', 'item_image')
    list_editable = ('item_image',)   # 👈 allow direct change in admin list

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'product_qty', 'created_at')

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')