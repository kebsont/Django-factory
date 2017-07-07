from django.shortcuts import render
 

def index(request):
	return render(request, 'pages/index.html')

def annonces(request):
	return render(request, 'pages/annonces.html')

def contact(request):
	return render(request, 'pages/contact.html')