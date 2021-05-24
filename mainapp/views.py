from django.shortcuts import render
from mainapp.models import Product, ProductCategory, Team

# Create your views here.

"""
def main(request):
    context = {'title': 'Main',
               'products': [
                   {'name': 'ASSASIN’S CREED:', 'nameSpan': 'Rogue', 'alt': 'ASSASIN’S CREED', 'image': 'img/pryamougolnik_8_186.jpg', 'click': 'product'},
                   {'name': 'Tomb Raider', 'nameSpan': '', 'alt': 'Tomb Raider', 'image': 'img/pryamougolnik_8_178.jpg', 'click': 'product'},
                   {'name': 'Ryse:', 'nameSpan': 'Son Of Rome', 'alt': 'Ryse', 'image': 'img/pryamougolnik_8_183.jpg', 'click': 'product'},
                   {'name': 'World Of Warcraft:', 'nameSpan': 'Wrath Of The Linch King', 'alt': 'World Of Warcraft', 'image': 'img/pryamougolnik_8_189.jpg', 'click': 'product'},
               ],
               'team': [
                   {'name': 'Mary Jane', 'alt': 'Mary Jane', 'image': 'img/pryamougolnik_6_127.jpg'},
                   {'name': 'Peter Parker', 'alt': 'Peter Parker', 'image': 'img/pryamougolnik_6_128.jpg'},
                   {'name': 'John Watson', 'alt': 'John Watson', 'image': 'img/pryamougolnik_6_129.jpg'},
                   {'name': 'Steven Wilson', 'alt': 'Steven Wilson', 'image': 'img/pryamougolnik_6_130.jpg'},
               ]
               }
    return render(request, 'mainapp/base.html', context)
"""

def main(request):
    context = {
        'title': 'Main',
        'products': Product.objects.all(),
        'team': Team.objects.all(),
        }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'title': 'Games',
               'products': Product.objects.all(),

               'discount_first':
                   {'name': 'CALL OF DUTY:', 'nameSpan': 'Modern Warfare 3', 'price': '$14.44', 'priceSpan': '$28.90', 'alt': 'CALL OF DUTY', 'image': 'img/pryamougolnik_25_1380.png',
                    'click': 'product'}
               ,

               'discount_second':
                   {'name': 'MEDAL OF HONOR', 'nameSpan': '', 'alt': 'BATTLEFIELD 1', 'price': '$15.96', 'priceSpan': '$29.99', 'image': 'img/pryamougolnik_25_1381.png',
                    'click': 'product'}

               }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {'title': 'Contact Us'}
    return render(request, 'mainapp/contacts.html', context)


def product(request):
    context = {'title': 'Game'}
    return render(request, 'mainapp/product.html', context)
