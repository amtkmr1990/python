'''
import socket


class Resolver:

    def __init__(self):

        self._cache = {}

    def __call__(self, hostname):
        if hostname not in self._cache:
            self._cache[hostname] = socket.gethostbyname(hostname)
        return self._cache[hostname]

g = 'global'
def outer():

    g = 'local'
    def inner():
        nonlocal g
        g = 'inner'
        print(g)
    inner()
    print(g)
outer()
print(g)
'''

class Student:

    def __init__(self, name):
        self.name = name
        self._age = None
        self._grade = None
    @property
    def grade(self):
        return self._grade
    @property
    def age(self):
        return self._age

    @grade.setter
    def grade(self, value):
        self._grade = value

    @age.setter
    def age(self, value):
        self._age = value



























