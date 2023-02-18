"""
All files in folder: ebookstore.py, database.py & ebookstore_functions.py
necessary for program.
"""
from database import *
from ebookstore_functions import *

# default books to populate table when empty.
default_books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                 (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
                 (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
                 (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
                 (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
                 (3006, 'Jabberwocky', 'Lewis Carroll', 71)]

# create/connect to database object and create table books.
db = Database("ebookstore.db")
db.create_table()

data = db.execute("SELECT * FROM books").fetchall()

# if table is empty, populate with default books.
if len(data) == 0:
    db.executemany("INSERT OR IGNORE INTO books (id, title, author, qty) VALUES (?,?,?,?)", default_books)

while True:
    print('''
        Select One of the Following Options Below:
            
        add - Enter Book into Database
        update - Update Book in Database
        delete - Delete Book in Database
        search - Search for a Book
        exit - Exit Program
        ''')

    menu = input("\nWhich Option Would You Like to Choose: ").lower()

    if menu == "add":
        while True:
            # validate all user input for new book details.
            add_id = id_validation(input("Enter the Book ID: "))
            if add_id is None:
                print("\n\tID must be a 4-Digit Integer!\n")
                continue
            add_title = input("Enter the book title: ")
            if len(add_title) == 0:
                print("\n\tTitle Field Cannot be Empty\n")
                continue
            add_author = input("Enter the book author: ")
            if len(add_author) == 0:
                print("\n\tAuthor Field Cannot be Empty\n")
                continue
            add_qty = qty_validation(input("Enter the book quantity: "))
            if add_qty is None:
                print("\n\tQuantity must be an Integer between 0 and 500!\n")
                continue
            # add book and commit.
            add_book(db, add_id, add_title, add_author, add_qty)
            db.commit()
            break
    elif menu == "update":
        while True:
            # validate user update details.
            update_id = id_validation(input("Enter ID of the Book to Update: "))
            if update_id is None:
                print("\n\tID must be a 4 Digit Integer!\n")
                continue
            update_qty = qty_validation(input("Enter Updated Quantity: "))
            if update_qty is None:
                print("\n\tQuantity must be an Integer between 0 and 500!\n")
                continue
            # update book and commit.
            update_book(db, update_id, update_qty)
            db.commit()
            break
    elif menu == "delete":
        while True:
            # validate user delete details.
            del_id = id_validation(input("Enter ID of the Book to Delete: "))
            if del_id is None:
                print("\n\tID must be a 4-Digit Integer!\n")
                continue
            # delete book and commit.
            delete_book(db, del_id)
            db.commit()
            break
    elif menu == "search":
        search_choice = input("Enter 'id', 'title', or 'author' to search by: ").lower()
        search_result = search_books(db, search_choice)
        # if book found print details, else print invalid search input.
        if search_result:
            print("\nResults:")
            for book in search_result:
                print(f'''
                ==============================
                ID: {book[0]} 
                Title: {book[1]}
                Author: {book[2]}
                Qty: {book[3]}
                ==============================
                ''')
        else:
            print('''
            Invalid Selection!
            No results found!
            ''')
    elif menu == "exit":
        # close connection and exit program.
        db.close_connection()
        print('\n\tGoodbye!!!')
        break
    else:
        print("\n\tYou Have Made an Invalid Choice, Please Try again!\n")
