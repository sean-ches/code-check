import math

class Base:
    def __init__(self):
        self.radius = int(input("Enter radius:"))
        self.PI = math.pi

    def getRadius(self):
        return self.radius


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


results = []
while True:
    shape = input('Select shape to calculate - "SPH", "CYL" or "CAP", type "DONE" when done:')
    if shape == 'SPH':
        sphere_volume = Sphere()
        print("Volume of sphere:", sphere_volume.getVolume())
        vol_result = {'Radius': sphere_volume.getRadius(), 'Volume': sphere_volume.getVolume(), 'Shape': 'Sphere'}

    elif shape == 'CYL':
        cyl_volume = Cylinder()
        print("Volume of cylinder:", cyl_volume.getVolume())
        vol_result = {'Radius': cyl_volume.getRadius(), 'Volume': cyl_volume.getVolume(), 'Shape': 'Cylinder'}

    elif shape == 'CAP':
        cap_volume = SphereCap()
        print("Volume of sphere cap:", cap_volume.getVolume())
        vol_result = {'Radius': cap_volume.getRadius(), 'Volume': cap_volume.getVolume(), 'Shape': 'Cap'}

    elif shape == 'DONE':
        break

    else:
        print("Unrecognized shape, try again!")
        continue
    print(vol_result)
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
