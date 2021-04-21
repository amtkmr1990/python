from utils import database


user_choice = """
select any option 

a = add book 
l = list books
r = mark a book as read
d = delete book 
q = quit 

Enter your choice : 
"""


def menu():
    choice = input(user_choice)
    while choice != 'q':
        if choice == 'a':
            add_book()
        elif choice == 'l':
            list_books()
        elif choice == 'r':
            read_book()
        elif choice == 'd':
            delete_book()
        else:
            print("Invalid Option. Try again ....")
        choice = input ( user_choice )


def add_book():
    book = input("Enter the book name : ")
    author = input("Enter the author name : ")
    database.add(book, author)

def list_books():
    print(database.list())

def read_book():
    book = input("Enter the book : ")
    database.read(book)

def delete_book():
    book = input ("Enter the book : ")
    database.delete(book)

menu()
