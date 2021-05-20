from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCategoryEditForm
from mainapp.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    selected_user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {'form': form,
               'selected_user': selected_user,
               }

    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))

@user_passes_test(lambda u: u.is_superuser)
def admin_users_restore(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))


def admin_categories_read(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)

def admin_categories_create(request):
    if request.method == 'POST':
        form = ProductCategoryEditForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))
    else:
        form = ProductCategoryEditForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)

def admin_categories_update(request, category_id):
    current_category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = ProductCategoryEditForm(data=request.POST, instance=current_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))
    else:
        form = ProductCategoryEditForm(instance=current_category)

    context = {'form': form,
               'current_category': current_category,
               }

    return render(request, 'adminapp/admin-categories-update-delete.html', context)

def admin_categories_remove(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))

def admin_categories_restore(request, category_id):
    user = User.objects.get(id=category_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))
