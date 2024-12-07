from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Book

print("views reached")

def home(request):
    print("home.html is rendered")
    return render(request, 'home.html')

def manage_authors(request):
    if request.method == "POST":
        action = request.POST.get('action')
        author_id = request.POST.get('author_id')
        author_name = request.POST.get('author_name')


        # Handle the form submission based on the action
        if action == 'add':
            # Add author logic
            pass
        elif action == 'delete':
            # Delete author logic
            pass
        elif action == 'update':
            # Update author logic
            pass

        return HttpResponse("Form submitted successfully.")
    
    return render(request, 'manage_authors.html')

def manage_books(request):
    if request.method == "POST":
        action = request.POST.get('action')
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        language = request.POST.get('language')
        page_num = request.POST.get('page_num')
        publisher = request.POST.get('publisher')
        library_id = request.POST.get('library_id')


        # Handle the form submission based on the action
        if action == 'add':
            # Add author logic
            pass
        elif action == 'delete':
            # Delete author logic
            pass
        elif action == 'update':
            # Update author logic
            pass

        return HttpResponse("Form submitted successfully.")

    return render(request, 'manage_books.html')

def manage_members(request):
    if request.method == "POST":
        action = request.POST.get('action')
        member_id = request.POST.get('member_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        phone_number = request.POST.get('phone_number')
        membership_date = request.POST.get('membership_date')


        # Handle the form submission based on the action
        if action == 'add':
            # Add author logic
            pass
        elif action == 'delete':
            # Delete author logic
            pass
        elif action == 'update':
            # Update author logic
            pass

        return HttpResponse("Form submitted successfully.")
    
    return render(request, 'manage_members.html')

def loan_book(request):
    if request.method == "POST":
        action = request.POST.get('action')
        loan_id = request.POST.get('loan_id')
        book_id = request.POST.get('book_id')
        member_id = request.POST.get('member_id')
        loan_date = request.POST.get('loan_date')
        due_date = request.POST.get('due_date')
        return_date = request.POST.get('return_date')

        # Handle the form submission based on the action
        if action == 'add':
            # Add author logic
            pass
        elif action == 'delete':
            # Delete author logic
            pass
        elif action == 'update':
            # Update author logic
            pass

        return HttpResponse("Form submitted successfully.")
    
    return render(request, 'loan_book.html')


def display_book(request, book_id):
    """
    Fetch the book details from the database and render them on the page.
    """
    # Fetch the book or return a 404 page if it doesn't exist
    book = get_object_or_404(Book, pk=book_id)

    # Pass the book data to the display page
    return render(request, 'display_book.html', {'book': book})