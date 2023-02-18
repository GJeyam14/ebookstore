# ebookstore functions.
# function validates 4-digit ID.
def id_validation(input_id):
    if not input_id.isnumeric():
        return None
    elif len(input_id) != 4:
        return None
    else:
        return int(input_id)


# function validates quantity.
def qty_validation(qty):
    if not qty.isnumeric():
        return None
    elif int(qty) > 500:
        return None
    else:
        return int(qty)


# function adds book to table if it does not already exist.
def add_book(book_db, book_id, title, author, qty):
    query_exist = "SELECT * FROM books WHERE id=? OR title=?"
    result = book_db.execute(query_exist, (book_id, title)).fetchall()
    if result:
        print(f"\n\tA Book with Title '{title}' or ID '{book_id}' already exists.\n")
    else:
        query_add = "INSERT INTO books (id, title, author, qty) VALUES (?,?,?,?)"
        book_db.execute(query_add, (book_id, title, author, qty))
        print("\n\tBook Successfully Added!\n")


"""
Update book function only updates quantity, if book exists in database. 
This will be utilised as books are sold and re-stocked.
Didn't seem useful to alter book characteristics that are unlikely to change.
If there are mistakes for a book's details in the table. 
The delete and add functions can be used to address this. 
"""


def update_book(book_db, book_id, qty):
    query_exist = "SELECT * FROM books WHERE id=?"
    result = book_db.execute(query_exist, (book_id,)).fetchall()
    if not result:
        print(f"\n\tBook Does Not Exist in Database!\n")
    else:
        query_update = "UPDATE books SET qty=? WHERE id=?"
        book_db.execute(query_update, (qty, book_id))
        print(f"\n\tBook ID:{book_id} - QTY has been Updated!\n")


# function deletes a book if it exists in the database.
def delete_book(book_db, book_id):
    query_exist = "SELECT * FROM books WHERE id=?"
    result = book_db.execute(query_exist, (book_id,)).fetchall()
    if not result:
        print(f"\n\tBook Does Not Exist in Database!\n")
    else:
        query_del = "DELETE FROM books WHERE id=?"
        book_db.execute(query_del, (book_id,))
        print(f"\n\tBook ID: {book_id} has been deleted from Database!\n")


# function searches database based on id, title or author and returns matches.
def search_books(book_db, search_criteria):
    if search_criteria == 'id':
        while True:
            search_id = id_validation(input("Enter the Book ID: "))
            if search_id is None:
                print("\n\tID must be a 4-Digit Integer!\n")
                continue
            else:
                break
        book_db.execute("SELECT * FROM books WHERE id = ?", (search_id,))

    elif search_criteria == 'title':
        search_title = input("Enter the Book Title: ")
        book_db.execute("SELECT * FROM books WHERE title = ?", (search_title,))

    elif search_criteria == 'author':
        search_author = input("Enter the Book Author: ")
        book_db.execute("SELECT * FROM books WHERE author = ?", (search_author,))

    return book_db.fetchall()
