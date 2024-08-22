from django.contrib import admin
from . models import Product, MyModel, Offers

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')

admin.site.register(Product,ProductAdmin)
admin.site.register(MyModel, MyModelAdmin)