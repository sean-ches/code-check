shape = input('Enter shape to calculate, must be "SQUARE", "TRIANGLE", "RECTANGLE", "TRAPEZOID":')

class Calc():

    base = int(input('Enter base:'))
    height = int(input('Enter height:'))
    if shape == 'TRAPEZOID' : base2 = int(input('Enter second base size:'))

    def __init__(self, height, base):
        self.height = height
        self.base = base

class Square(Calc):

    def cal():
        return print('Calculated square area:', Calc.base * Calc.height)

class Triangle(Calc):

    def cal():
        return print('Calculated triangle area:', Calc.base * Calc.height / 2)

class Rectangle(Calc):

    def cal():
        return print('Calculated rectangle area:', Calc.base * Calc.height)

class Trapezoid(Calc):

    def cal():
        return print('Calculated trapezoid area:', (Calc.base + Calc.base2) * Calc.height / 2)

if shape == 'SQUARE' : Square.cal()
if shape == 'TRIANGLE' : Triangle.cal()
if shape == 'RECTANGLE' : Rectangle.cal()
if shape == 'TRAPEZOID' : Trapezoid.cal()
