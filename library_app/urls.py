from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loan_book/', views.loan_book, name='loan_book'),
    path('manage_authors/', views.manage_authors, name='manage_authors'),
    path('manage_books/', views.manage_books, name='manage_books'),
    path('manage_members/', views.manage_members, name='manage_members'),
    path('display_book/', views.display_book, name='display_book'),
]