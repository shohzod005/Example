from django.contrib import admin
from .models  import *
uneditable_fields = ('id', 'date_created', 'date_updated')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug","desc")
    fields = [field.name for field in Category._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug","desc","price")

    fields = [field.name for field in Category._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("category","status", "quen")
    fields = [field.name for field in Category._meta.fields]

@admin.register(CostumUser)
class CostumUserAdmin(admin.ModelAdmin):
    list_display = ("fullnamne","email", "phone_number","address")
    fields = [field.name for field in Category._meta.fields]

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ("custmuser","totol_price")
    fields = [field.name for field in Category._meta.fields]

@admin.register(product_photo)
class product_photoAdmin(admin.ModelAdmin):
    list_display = ("product","thumb", "lorg_pc")
    fields = [field.name for field in Category._meta.fields]

