from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.db import connection
from django.urls import reverse

def home(request):
    if request.method == "GET":
        
        genre = request.GET.get('genre', '').strip()
        author = request.GET.get('author', '').strip()
        pages = request.GET.get('pages', '').strip()

        
        query_params = {}
        if genre:
            query_params['genre'] = genre
        if author:
            query_params['author'] = author
        if pages:
            query_params['pages'] = pages

        
        if query_params:
            query_string = '&'.join([f"{key}={value}" for key, value in query_params.items()])
            return HttpResponseRedirect(reverse('display_book') + f"?{query_string}")

    # If no filters are provided, just render the home page
    return render(request, 'home.html')

def home(request):
    print("home.html is rendered")
    return render(request, 'home.html')

#manipulating authors
def manage_authors(request):
    if request.method == "POST":
        action = request.POST.get('action')
        author_id = request.POST.get('author_id')
        author_name = request.POST.get('author_name')


        # based on the action : 
        with connection.cursor() as cursor:
            if action == 'add':
                if author_name:
                    cursor.execute("INSERT INTO authors (author_id, author_name) VALUES (%s, %s)", [author_id, author_name]) 
                    return HttpResponse("Author added successfully")
                else:
                    return HttpResponse(f"Author name is required to add authors", status=400)
            elif action == 'delete':
                
                if author_id:
                    cursor.execute("DELETE FROM authors WHERE author_id = %s", [author_id]) 
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Author with ID {author_id} deleted successfully.")
                    else:
                        return HttpResponse("Author not found.", status=404)
                else:
                    return HttpResponse("Author ID is required.", status=400)
            elif action == 'update':
                
                if author_id and author_name:
                    cursor.execute(
                        "UPDATE authors SET author_name = %s WHERE author_id = %s",
                        [author_name, author_id]
                    )
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Author with ID {author_id} updated to '{author_name}'.")
                    else:
                        return HttpResponse("Author not found.", status=404)
                else:
                    return HttpResponse("Author ID and name are required.", status=400)

        return HttpResponse("Form submitted successfully.")
    
    return render(request, 'manage_authors.html')

#manipulating books
def manage_books(request):
    if request.method == "POST":
        action = request.POST.get('action')
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        language = request.POST.get('language')
        page_num = request.POST.get('page_num')
        publisher = request.POST.get('publisher')
        library_id = request.POST.get('library_id')
        author_id = request.POST.get('author_id')


        with connection.cursor() as cursor:
            if action == 'add':
                
                if title and language and page_num and publisher and library_id:
                    cursor.execute(
                        """
                        INSERT INTO books (book_id, title, author_id, language, page_num, publisher, library_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        [book_id, title, author_id, language, page_num, publisher, library_id]
                    )
                    return HttpResponse(f"Book '{title}' added successfully.")
                else:
                    return HttpResponse("All fields are required to add a book.", status=400)

            elif action == 'delete':
                
                if book_id:
                    cursor.execute("DELETE FROM books WHERE book_id = %s", [book_id])
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Book with ID {book_id} deleted successfully.")
                    else:
                        return HttpResponse("Book not found.", status=404)
                else:
                    return HttpResponse("Book ID is required.", status=400)

            elif action == 'update':
                
                if book_id and title and language and page_num and publisher and library_id:
                    cursor.execute(
                        """
                        UPDATE books 
                        SET title = %s, language = %s, page_num = %s, publisher = %s, library_id = %s 
                        WHERE book_id = %s
                        """,
                        [title, language, page_num, publisher, library_id, book_id]
                    )
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Book with ID {book_id} updated successfully.")
                    else:
                        return HttpResponse("Book not found.", status=404)
                else:
                    return HttpResponse("All fields are required to update a book.", status=400)

        return HttpResponse("Invalid action.", status=400)

    
    with connection.cursor() as cursor:
        cursor.execute("SELECT book_id, title, language, page_num, publisher, library_id FROM books")
        books = cursor.fetchall()

    return render(request, 'manage_books.html', {'books': books})

#manipulating members
def manage_members(request):
    if request.method == "POST":
        action = request.POST.get('action')
        member_id = request.POST.get('member_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        phone_num = request.POST.get('phone_num')
        membership_date = request.POST.get('membership_date')

        with connection.cursor() as cursor:
            if action == 'add':
                
                if first_name and last_name and mail and phone_num and membership_date:
                    cursor.execute(
                        """
                        INSERT INTO members (first_name, last_name, mail, phone_num, membership_date) 
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        [first_name, last_name, mail, phone_num, membership_date]
                    )
                    return HttpResponse(f"Member '{first_name} {last_name}' added successfully.")
                else:
                    return HttpResponse("All fields are required to add a member.", status=400)

            elif action == 'delete':
                
                if member_id:
                    cursor.execute("DELETE FROM members WHERE member_id = %s", [member_id])
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Member with ID {member_id} deleted successfully.")
                    else:
                        return HttpResponse("Member not found.", status=404)
                else:
                    return HttpResponse("Member ID is required.", status=400)

            elif action == 'update':
                
                if member_id and first_name and last_name and mail and phone_num and membership_date:
                    cursor.execute(
                        """
                        UPDATE members 
                        SET first_name = %s, last_name = %s, mail = %s, phone_num = %s, membership_date = %s 
                        WHERE member_id = %s
                        """,
                        [first_name, last_name, mail, phone_num, membership_date, member_id]
                    )
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Member with ID {member_id} updated successfully.")
                    else:
                        return HttpResponse("Member not found.", status=404)
                else:
                    return HttpResponse("All fields are required to update a member.", status=400)

        return HttpResponse("Invalid action.", status=400)

    # Fetch members for display
    with connection.cursor() as cursor:
        cursor.execute("SELECT member_id, first_name, last_name, mail, phone_num, membership_date FROM members")
        members = cursor.fetchall()

    return render(request, 'manage_members.html', {'members': members})

#manipulating loans
def loan_book(request):
    if request.method == "POST":
        action = request.POST.get('action')
        loan_id = request.POST.get('loan_id')
        book_id = request.POST.get('book_id')
        member_id = request.POST.get('member_id')
        loan_date = request.POST.get('loan_date')
        due_date = request.POST.get('due_date')
        return_date = request.POST.get('return_date')

        with connection.cursor() as cursor:
            if action == 'add':
                
                if book_id and member_id and loan_date and due_date:
                    if return_date =='':
                        cursor.execute(
                            """
                            INSERT INTO loans (loan_id, book_id, member_id, loan_date, due_date) 
                            VALUES (%s,%s, %s, %s, %s)
                            """,
                            [loan_id,book_id, member_id, loan_date, due_date]
                        )
                    else:
                        cursor.execute(
                            """
                            INSERT INTO loans (loan_id, book_id, member_id, loan_date, due_date, return_date) 
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            [loan_id, book_id, member_id, loan_date, due_date,return_date]
                        )

                    return HttpResponse(f"Loan added successfully for Book ID {book_id} and Member ID {member_id}.")
                else:
                    return HttpResponse("Book ID, Member ID, Loan Date, and Due Date are required.", status=400)

            elif action == 'delete':
                
                if loan_id:
                    cursor.execute("DELETE FROM loans WHERE loan_id = %s", [loan_id])
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Loan with ID {loan_id} deleted successfully.")
                    else:
                        return HttpResponse("Loan not found.", status=404)
                else:
                    return HttpResponse("Loan ID is required.", status=400)

            elif action == 'update':
                
                if loan_id and book_id and member_id and loan_date and due_date:
                    cursor.execute(
                        """
                        UPDATE loans 
                        SET book_id = %s, member_id = %s, loan_date = %s, due_date = %s, return_date = %s 
                        WHERE loan_id = %s
                        """,
                        [book_id, member_id, loan_date, due_date, return_date, loan_id]
                    )
                    if cursor.rowcount > 0:
                        return HttpResponse(f"Loan with ID {loan_id} updated successfully.")
                    else:
                        return HttpResponse("Loan not found.", status=404)
                else:
                    return HttpResponse("All fields are required to update a loan.", status=400)

        return HttpResponse("Invalid action.", status=400)

    # Fetch loans for display
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT l.loan_id, l.book_id, b.title, l.member_id, m.first_name, m.last_name, 
                   l.loan_date, l.due_date, l.return_date
            FROM loans l
            JOIN books b ON l.book_id = b.book_id
            JOIN members m ON l.member_id = m.member_id
            """
        )
        loans = cursor.fetchall()

    return render(request, 'loan_book.html', {'loans': loans})


def display_book(request):
    # Extract filter parameters from the GET request
    genre = request.GET.get('genre', '')
    author = request.GET.get('author', '')
    min_pages = request.GET.get('min_pages', 0)
    max_pages = request.GET.get('max_pages', 10000)

    # Base SQL query to include the author's name
    sql_query = """
        SELECT b.*, a.author_name 
        FROM books AS b
        JOIN authors AS a ON b.author_id = a.author_id
        WHERE 1=1
    """
    params = []


    # Apply filters dynamically
    if genre:
        sql_query += " AND genre LIKE %s"
        params.append(f"%{genre}%")  # For case-insensitive search
    if author:
        sql_query += " AND author_name LIKE %s"
        params.append(f"%{author}%")
    if min_pages:
        sql_query += " AND page_num >= %s"
        params.append(min_pages)
    if max_pages:
        sql_query += " AND page_num <= %s"
        params.append(max_pages)

    # Execute the query
    with connection.cursor() as cursor:
        cursor.execute(sql_query, params)
        columns = [col[0] for col in cursor.description]  # Get column names
        books = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Format results as a list of dicts

    context = {
        'books': books,  # Pass filtered books to the template
        'filters': {
            'genre': genre,
            'author': author,
            'min_pages': min_pages,
            'max_pages': max_pages,
        }
    }

    return render(request, 'display_book.html', context)
