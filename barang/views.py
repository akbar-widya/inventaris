from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item, Kategori
from .forms import ItemForm # Wajib diimpor

@login_required
def daftar_item(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(nama__icontains=query)
    else:
        items = Item.objects.all()

    # 1. Inisiasi form kosong
    form = ItemForm() 

    if request.headers.get('HX-Request'):
        return render(request, 'barang/partial_item.html', {'items': items})
    
    # 2. Variabel 'form' WAJIB dimasukkan ke dalam dictionary ini
    return render(request, 'barang/daftar_item.html', {'items': items, 'form': form})

@login_required
def tambah_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            items = Item.objects.all()
            return render(request, 'barang/partial_item.html', {'items': items})

@login_required    
def hapus_item(request, id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=id)
        item.delete()
        return HttpResponse('')

@login_required
def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'barang/item_row.html', {'item': item})

@login_required
def edit_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        # Simpan perubahan
        item.nama = request.POST.get('nama')
        item.kategori_id = request.POST.get('kategori')
        item.stok = request.POST.get('stok')
        item.harga = request.POST.get('harga')
        item.save()
        return render(request, 'barang/item_row.html', {'item': item})
    
    # Jika GET, kirimkan form edit beserta daftar kategori untuk dropdown
    kategoris = Kategori.objects.all()
    return render(request, 'barang/item_edit.html', {'item': item, 'kategoris': kategoris})