from django.contrib import admin
from django.urls import path

from .views import ModuleGetAll, ModuleCreate, GetModule, ModuleDelete, UpdateModule

urlpatterns = [
    path('module/', ModuleGetAll.as_view(), name='module'),
    path('module/<int:id>', GetModule.as_view(), name='get_module'),
    path('module/create/', ModuleCreate.as_view(), name='module_create'),
    path('module/delete/<int:id>', ModuleDelete.as_view(), name='delete_create'),
    path('module/update/<int:pk>', UpdateModule.as_view(), name='update_create'),
]