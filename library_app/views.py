from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def borrow_return(request):
    return render(request, 'borrow_return.html')

def about(request):
    return render(request, 'about.html')
