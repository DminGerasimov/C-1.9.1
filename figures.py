import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

