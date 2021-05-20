from django.contrib import admin
from mainapp.models import Product, ProductCategory, Team


admin.site.register(ProductCategory)
admin.site.register(Team)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    ordering = ('-name',)
    search_fields = ('name',)
