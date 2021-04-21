
"""
name,author,0\n
name,author,0\n
name,author,0\n

"""
books = "books.txt"


def add(name,author):
    with open(books,'a') as file:
        file.write(f"{name},{author},{'0'}\n")


def list():
    with open(books,'r') as file:
        content = file.read()
    print(type(content))
    return content


def read(book):
    with open(books,'r') as file:
        content = [i.strip().split(',') for i in file.readlines()]

    for i in content:
        if i[0] == book:
            i[2] = '1'

    with open(books,'w') as file:
        for i in content:
            file.write(f'{i[0]},{i[1]},{i[2]}\n')


def delete(name):
    with open(books,'r') as file:
        content = [ i.strip().split(',') for i in file.readlines()]

    for i,j in enumerate(content):
        if j[0] == name:
            del content[i]

    with open(books,'w') as file:
        for i in content:
            file.write(f'{i[0]},{i[1]},{i[2]}\n')