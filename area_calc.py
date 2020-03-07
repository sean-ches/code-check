class Calc():

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

     def __init__(self):
         super().__init__()
         self.base2 = int(input("Enter second base for Trapezoid:"))

     def getArea(self):
         return (self.base + self.base2) * self.height / 2


results = []
while True:
    shape = input('Enter shape to calculate, must be "SQUARE", "TRIANGLE", "RECTANGLE" or "TRAPEZOID":')

    if shape == 'SQUARE':
        square = Square()
        print ("Square Area is" , square.getArea(), 'Type "DONE" when finished.')
        results.append(square.getArea())
        continue
    elif shape == 'TRIANGLE':
        triangle = Triangle()
        print ("Triangle Area is" , triangle.getArea(), 'Type "DONE" when finished.')
        results.append(triangle.getArea())
        continue
    elif shape == 'RECTANGLE':
        rectangle = Rectangle()
        print ("Rectangle Area is", rectangle.getArea(), 'Type "DONE" when finished.')
        results.append(rectangle.getArea())
        continue
    elif shape == 'TRAPEZOID':
        trapezoid = Trapezoid()
        print ("Trapezoid Area is", trapezoid.getArea(), 'Type "DONE" when finished.')
        results.append(trapezoid.getArea())
        continue
    elif shape == 'DONE': break

    else:
        print('Unrecognized shape, try again.')
        continue

print('Process done! \nMaximum element is:', max(results),'\nMinimum element is:',min(results))