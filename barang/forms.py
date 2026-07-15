from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nama', 'kategori', 'stok', 'harga']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nama Barang'}),
            'kategori': forms.Select(attrs={'class': 'form-input'}),
            'stok': forms.NumberInput(attrs={'class': 'form-input'}),
            'harga': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
        }