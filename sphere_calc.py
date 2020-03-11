class Base:
    def __init__(self):
        self.radius = int(input("Enter radius:"))
        self.PI = 3.14


class Sphere(Base):

    def getVolume(self):
        return (3 / 4) * self.PI * self.radius ** 3


class Cylinder(Base):

    def __init__(self):
        super().__init__()
        self.height = int(input('Enter height:'))

    def getVolume(self):
        return self.PI * self.radius ** 2 * self.height


class SphereCap(Base):

    def __init__(self):
        super().__init__()
        self.height = int(input('Enter height:'))

    def getVolume(self):
        return (self.PI * self.height ** 2) / 3 * (3 * self.radius - self.height)


while True:
    shape = input('Select shape to calculate:')

    if shape == 'SPH':
        sphere_area = Sphere()
        print("Volume of sphere:", sphere_area.getVolume())
        break

    elif shape == 'CYL':
        cyl_area = Cylinder()
        print("Volume of cylinder:", cyl_area.getVolume())
        break

    elif shape == 'CAP':
        cap_area = SphereCap()
        print("Volume of sphere cap:", cap_area.getVolume())
        break

    else:
        print("Unrecognized shape, try again!")
        continue
