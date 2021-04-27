from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True) #строка
    description = models.TextField(blank=True) #blank-пустой. может быть заполнено или нет

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)  # строка
    image = models.ImageField(upload_to='products_images', blank=True) #upload_to - куда будет загружено изображение
    description = models.CharField(max_length=64, blank=True)  # blank-пустой. может быть заполнено или нет
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) #protect -не можем удалить ктегорию
    # пока есть хотябы 1 продукт принадлежащий этой категории

def __str__(self):
    return f'{self.name} | {self.category.name}'