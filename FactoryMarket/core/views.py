from django.shortcuts import render
from .models import Categorie

def index(request):
	categ = Categorie.objects.all()
	return render(request, 'pages/index.html',   {'categ': categ})

def annonces(request):
	return render(request, 'pages/annonces.html')

def contact(request):
	return render(request, 'pages/contact.html')