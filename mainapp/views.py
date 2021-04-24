from django.shortcuts import render


# Create your views here.

def main(request):
    context = {'title': 'Main'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'Games',}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {'title': 'Contact Us'}
    return render(request, 'mainapp/contacts.html', context)


def product(request):
    context = {'title': 'Game'}
    return render(request, 'mainapp/product.html', context)

def test(request):
    context = context = {'title': 'test',
               'products': [
                   {'name': 'BATTLEFIELD 1'},
                   {'name': 'STAR WARS: Battlefront II'},
                   {'name': 'BATTLEFIELD 4'},
                   {'name': 'WORLD OF TANKS'},
                   {'name': 'ASSASIN’S CREED:Rogue'},
                   {'name': 'FOR HONOR'},
                   {'name': 'WORLD OF WARSHIPS'},
                   {'name': 'CALL OF DUTY:Infinite Warface'},
               ]
               }
    return render(request, 'mainapp/test.html', context)
