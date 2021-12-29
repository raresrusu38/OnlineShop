from django.contrib import admin
from .models import *


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    
    
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('code',)


class PriceFilterAdmin(admin.ModelAdmin):
    list_display = ('price',)
    list_filter = ('price',)

    
class ImagesTublerinline(admin.TabularInline):
    model = Images
    
    
class TagTublerinline(admin.TabularInline):
    model = Tag


class ProductAdmin(admin.ModelAdmin):
    inline = [ImagesTublerinline, TagTublerinline]
    
    
admin.site.register(Images)
admin.site.register(Tag)

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Price_Filter, PriceFilterAdmin)
admin.site.register(Product, ProductAdmin)
