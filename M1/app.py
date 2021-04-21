"""
menu
a = add a movie
list = list movies
f = find a movie
q = qiut from program
"""

movies = []
def menu():

    user_ip = input('Enter your Choice : ')

    while user_ip != 'q':
        if user_ip == 'a':
            add()
        elif user_ip == 'l':
            show()
        elif user_ip == 'f':
            find()
        else:
            print('Invalid Input -- Please try again ...')

        user_ip = input ( 'Enter your Choice : ' )


def add():
    name = input("enter movie name : ")
    director = input("enter director name : ")
    year = int(input("enter the release year : "))

    movie = {
        'name': name,
        'director': director,
        'year': year
    }

    movies.append(movie)

    print(f" Movie added ... {movie}")


def show():
    print("We have movies ..... ")
    print(movies)


def find():
    findmovie = input("enter the movie you want ot search ....")
    for i in movies:
        print(i)
        if findmovie in i["name"]:
            print(i["name"])
        else:
            print("not found the movie ")
menu()

