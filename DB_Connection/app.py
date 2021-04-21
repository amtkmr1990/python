from utils import db_con

server = "localhost"
db = "dev"

def menu():
    ip = input("enter the option : ")
    while ip != 'q':
        if ip == 'a':
            add_book()
        elif ip == 'l':
            list_book()
        else:
            print("invalid input ")


def add_book():
    name = input("enter the book name : ")
    auther = input("enter the auther name : ")
    with db_con.Connect(server,db) as connection:
        cursor = connection.cursor()
        cursor.execute("insert into books values(?,?)",(name, auther) )

def list_book():
    with db_con.Connect(server,db) as connection:
        cursor = connection.cursor()
        cursor.execute("select * from books")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
menu()