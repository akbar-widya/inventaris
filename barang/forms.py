from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nama', 'kategori', 'stok', 'harga']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Barang'}),
            'kategori': forms.Select(attrs={'class': 'form-select'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }