from django.urls import path

from adminapp.views import index, admin_users_restore, admin_categories_update
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from adminapp.views import CategoriesListView, CategoriesCreateView,  admin_categories_remove, admin_categories_restore

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('admin-users-restore/<int:user_id>/', admin_users_restore, name='admin_users_restore'),

    path('admin-categories-read/', CategoriesListView.as_view(), name='admin_categories_read'),
    path('admin-categories-create/', CategoriesCreateView.as_view(), name='admin_categories_create'),
    path('admin-categories-update/<int:id>/', admin_categories_update, name='admin_categories_update'),
    path('admin-categories-remove/<int:category_id>/', admin_categories_remove, name='admin_categories_remove'),
    path('admin-categories-restore/<int:category_id>/', admin_categories_restore, name='admin_categories_restore'),
]
