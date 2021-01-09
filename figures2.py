from figures import Rectangle, Square, Circle

#прямоугольники
rect1 = Rectangle(2, 3)
rect2 = Rectangle(3, 4)

#штаны спанчбоба
square1 = Square(5)
square2 = Square(6)

#окружности
circle1 = Circle(6)
circle2 = Circle(7)


figures = [rect1, square1, circle1, rect2, circle2, square2 ]

for figure in figures:
    if isinstance(figure,Rectangle):
        print(f"Figure Rectangle with area {figure.get_area()}")
    elif isinstance(figure,Square):
            print(f"Figure Square with area {figure.get_area()}")
    elif isinstance(figure,Circle):
        print(f"Figure Circle with area {figure.get_area()}")
    else:
        print("Error in head)")
