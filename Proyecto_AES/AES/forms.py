from django import forms

class EncryptionForm(forms.Form):
    plaintext = forms.CharField(label='Texto a encriptar', widget=forms.Textarea)
    key = forms.CharField(label='Clave')

class DecryptionForm(forms.Form):
    ciphertext = forms.CharField(label='Texto a desencriptar', widget=forms.Textarea)
    key = forms.CharField(label='Clave')
