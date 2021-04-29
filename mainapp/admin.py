from django.contrib import admin
from mainapp.models import Product, ProductCategory, Team
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Team)
