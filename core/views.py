from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    
    return render(request, "core/home.html")

def blog(request):
    
    return render(request, "core/blog.html")

def single(request):
    
    return render(request, "core/single.html")

def contact_us(request):
    
    return render(request, "core/contact_us.html")

def horaactual(request):
    horario =""