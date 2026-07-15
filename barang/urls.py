from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_item, name='daftar_item'),
    path('tambah/', views.tambah_item, name='tambah_item'),
    path('hapus/<int:id>/', views.hapus_item, name='hapus_item'),
    path('item/<int:id>/', views.get_item, name='get_item'),
    path('item/<int:id>/edit/', views.edit_item, name='edit_item'),
]