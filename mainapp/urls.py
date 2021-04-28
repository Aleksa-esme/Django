from django.urls import path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'), #отображение каталогов товаров
    path('<int:id>/', products, name='product'),
]