from django.contrib import admin
from .models import MenuItems, Category, OrderModel
# Register your models here.
admin.site.register(MenuItems)
admin.site.register(Category)
admin.site.register(OrderModel)

