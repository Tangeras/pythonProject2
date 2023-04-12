from rectangle import Rectangle, Square, Circle
rect1=Rectangle(3,4)
rect2=Rectangle(12,5)

square1=Square(5)
square2=Square(10)

circle_1=Circle(3)
circle_2=Circle(7)

figures=[rect1, rect2, square1, square2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.getArea_square())
    elif isinstance(figure,Circle):
        print(figure.getArea_circle())
    else:
        print(figure.getArea())