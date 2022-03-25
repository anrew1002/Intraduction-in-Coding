import math
class hexagon():
    radius=0
    area=0
    def __init__(self,rad):
        self.radius=rad
        self.calc_area(rad)
    def calc_area(self,radius):
         self.area=radius**2 * 3 * math.sqrt(3)/2
    def set_radius(self,rad):
        if type(rad)==float or type(rad)==int:
            self.radius=rad
            self.calc_area(rad)
hex1=hexagon(3)
hex1.set_radius(4)
hex1.set_radius("frgrgr")
print(hex1.radius)
print(hex1.area)
print(type(hex1.area))
