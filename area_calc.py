shape = input('Enter shape to calculate, must be "SQUARE", "TRIANGLE", "RECTANGLE", "TRAPEZOID":')


class Calc():
    if shape == 'TRAPEZOID': base2 = int(input('Enter second base size:'))

    def __init__(self, height, base):
        self.height = height
        self.base = base
        base = int(input('Enter base:'))
        height = int(input('Enter height:'))


class Square(Calc):

    def __init__(self, height, base):
        super().__init__(height, base)

    def getArea(self):
        return self.base * self.height


class Triangle(Calc):

    def cal(self):
        return print('Calculated triangle area:', Calc.base * Calc.height / 2)


class Rectangle(Calc):

    def cal(self):
        return print('Calculated rectangle area:', Calc.base * Calc.height)


class Trapezoid(Calc):

    def cal(self):
        return print('Calculated trapezoid area:', (Calc.base + Calc.base2) * Calc.height / 2)


if shape == 'SQUARE': Square.getArea()
if shape == 'TRIANGLE': Triangle.cal()
if shape == 'RECTANGLE': Rectangle.cal()
if shape == 'TRAPEZOID': Trapezoid.cal()
