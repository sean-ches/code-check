class Base:
    def __init__(self):
        self.radius = int(input("Enter radius:"))
        self.PI = 3.14


class Sphere(Base):

    def getVolume(self):
        return (3 / 4) * self.PI * self.radius ** 3

    def getRadius(self):
        return self.radius


class Cylinder(Base):

    def __init__(self):
        super().__init__()
        self.height = int(input('Enter height:'))

    def getVolume(self):
        return self.PI * self.radius ** 2 * self.height

    def getRadius(self):
        return self.radius


class SphereCap(Base):

    def __init__(self):
        super().__init__()
        self.height = int(input('Enter height:'))

    def getVolume(self):
        return (self.PI * self.height ** 2) / 3 * (3 * self.radius - self.height)

    def getRadius(self):
        return self.radius


results = []
while True:
    shape = input('Select shape to calculate - "SPH", "CYL" or "CAP", type "DONE" when done:')

    if shape == 'SPH':
        sphere_area = Sphere()
        print("Volume of sphere:", sphere_area.getVolume())
        vol_result = {'Radius': sphere_area.getRadius(), 'Volume': sphere_area.getVolume(), 'Shape': 'Sphere'}

    elif shape == 'CYL':
        cyl_area = Cylinder()
        print("Volume of cylinder:", cyl_area.getVolume())
        vol_result = {'Radius': cyl_area.getRadius(), 'Volume': cyl_area.getVolume(), 'Shape': 'Cylinder'}

    elif shape == 'CAP':
        cap_area = SphereCap()
        print("Volume of sphere cap:", cap_area.getVolume())
        vol_result = {'Radius': cap_area.getRadius(), 'Volume': cap_area.getVolume(), 'Shape': 'Cap'}

    elif shape == 'DONE':
        break

    else:
        print("Unrecognized shape, try again!")
        continue
    results.append(vol_result)

radius = [result['Radius'] for result in results]
volume = [result['Volume'] for result in results]
if len(radius) == 0 or len(volume) == 0:
    print('Nothing to check, exiting program.')
    exit()

sum = 0
for vol in volume:
    sum = sum + vol

print('| Max volume result is:', max(volume))
print('| Min volume result is:', min(volume))
print('|\n| Max radius result is:', max(radius))
print('| Min radius result is:', min(radius))
print('|\n| Sum of all results is:', sum)
