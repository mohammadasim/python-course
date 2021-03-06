class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    
    def distance(self):
        # Tuple unpacking
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        result = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return result

    
    def slope(self):
        # Tuple unpacking
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        result = (y2 - y1) / (x2 - x1)
        return result

cor1 = (3,2)
cor2 = (8,10)
myline = Line(cor1,cor2)
print(myline.distance())
print(myline.slope())


class Cylinder:

    pi = 3.14159

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        h = self.height
        r = self.radius
        volume = Cylinder.pi * (r)**2 * h
        return volume  

    def surface_area(self):
        h = self.height
        r = self.radius
        surface_area = 2*Cylinder.pi*r*h + 2*Cylinder.pi*(r)**2
        return surface_area

mycylinder = Cylinder(2,3)
print(mycylinder.volume())
print(mycylinder.surface_area())