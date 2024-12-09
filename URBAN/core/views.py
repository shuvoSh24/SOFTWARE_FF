from django.shortcuts import render

def signin(request):
    return render(request, 'signin.html')

def register(request):
    return render(request, 'register.html')

def propertiesd(request):
    return render(request, 'properties-detail.html')

def properties(request):
    return render(request, 'properties.html')

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')
