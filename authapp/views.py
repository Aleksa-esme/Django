from django.shortcuts import render

def login(request):
    context = {'title': 'Authorizing'}
    return render(request, 'authapp/login.html', context)
