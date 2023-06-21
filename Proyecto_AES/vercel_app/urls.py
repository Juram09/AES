from django.urls import path
from AES import views

urlpatterns = [
    path('', views.home, name='index'),
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
]
