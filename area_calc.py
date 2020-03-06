shape = input('Enter shape to calculate, must be "SQUARE", "TRIANGLE", "RECTANGLE", "TRAPEZOID":')


class Calc():
#    if shape == 'TRAPEZOID': base2 = int(input('Enter second base size:'))

    def __init__(self):
        self.base = int(input('Enter base:'))
        self.height = int(input('Enter height:'))

class Square(Calc):

    def getArea(self):
        return self.base * self.height


class Triangle(Calc):

    def getArea(self):
        return self.base * self.height / 2


class Rectangle(Calc):

    def getArea(self):
        return self.base * self.height


class Trapezoid(Calc):

     def __init__(self, height, base, base2):
         super().__init__(height, base)
         self.base2 = int(input("Enter second base for Trapezoid:"))

     def getArea(self):
         return (self.base + self.base2) * self.height / 2


if shape == 'SQUARE':
    Square = Square()
    print ("Square Area is" , Square.getArea())
if shape == 'TRIANGLE':
    Triangle = Triangle()
    print ("Triangle Area is" , Triangle.getArea())
if shape == 'RECTANGLE':
    Rectangle = Rectangle()
    print ("Rectangle Area is", Rectangle.getArea())
if shape == 'TRAPEZOID':
    Trapezoid = Trapezoid()
    print ("Trapezoid Area is", Trapezoid.getArea())

