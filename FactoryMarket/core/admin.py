from django.contrib import admin

# Register your models here.
from .models import Annonces, Produits, Utilisateurs, Categorie,Utilisateurs
admin.site.register(Annonces)
admin.site.register(Produits)
admin.site.register(Categorie)
admin.site.register(Utilisateurs)
