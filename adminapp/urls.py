from django.urls import path

from adminapp.views import index, admin_users_read, admin_users_create, admin_users_update, admin_users_remove, admin_users_restore
from adminapp.views import admin_categories_read, admin_categories_create, admin_categories_update, admin_categories_remove, admin_categories_restore

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_users_read, name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('admin-users-remove/<int:user_id>/', admin_users_remove, name='admin_users_remove'),
    path('admin-users-restore/<int:user_id>/', admin_users_restore, name='admin_users_restore'),

    path('admin-categories-read/', admin_categories_read, name='admin_categories_read'),
    path('admin-categories-create/', admin_categories_create, name='admin_categories_create'),
    path('admin-categories-update/<int:category_id>/', admin_categories_update, name='admin_categories_update'),
    path('admin-categories-remove/<int:category_id>/', admin_categories_remove, name='admin_categories_remove'),
    path('admin-categories-restore/<int:category_id>/', admin_categories_restore, name='admin_categories_restore'),
]
