from django.shortcuts import render
from .forms import EncryptionForm, DecryptionForm
from .aes import encrypt, decrypt

def encrypt_view(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data['plaintext']
            key = form.cleaned_data['key']
            ciphertext = encrypt(plaintext, key)
            return render(request, 'encriptar.html', {'ciphertext': ciphertext})
    else:
        form = EncryptionForm()
    return render(request, 'encriptar.html', {'form': form})

def decrypt_view(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            ciphertext = form.cleaned_data['ciphertext']
            key = form.cleaned_data['key']
            plaintext = decrypt(ciphertext, key)
            return render(request, 'desencriptar.html', {'plaintext': plaintext})
    else:
        form = DecryptionForm()
    return render(request, 'desencriptar.html', {'form': form})
