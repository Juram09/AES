from django.shortcuts import render
from .forms import EncryptionForm, DecryptionForm
from .aes import encrypt, decrypt
def home(request):
    return render(request, 'home.html')

def encrypt_view(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data['plaintext']
            key = form.cleaned_data['key']
            print("Mensaje recibido:", plaintext)
            print("Clave recibida:", key)
            ciphertext = encrypt(plaintext, key)
            print("Mensaje Encriptado:", ciphertext)
            return render(request, 'encriptar.html', {'encrypted_message': ciphertext})
        else:
            print("Formulario inválido")
    else:
        form = EncryptionForm()
    return render(request, 'encriptar.html', {'form': form})

def decrypt_view(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            ciphertext = form.cleaned_data['ciphertext']
            key = form.cleaned_data['key']
            print("Texto cifrado recibido:", ciphertext)
            print("Clave recibida:", key)
            plaintext = decrypt(ciphertext, key)
            print("Texto desencriptado:", plaintext)
            return render(request, 'desencriptar.html', {'plaintext': plaintext})
        else:
            print("Formulario inválido")
    else:
        form = DecryptionForm()
    return render(request, 'desencriptar.html', {'form': form})
