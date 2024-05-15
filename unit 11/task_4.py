import math


class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        v = (4 / 3) * math.pi * (self.r**3)
        return v

    def get_square(self):
        s = 4 * math.pi * (self.r**2)
        return s

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.r = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        distance = math.sqrt(
            (x - self.x)**2 +
            (y - self.y)**2 +
            (z - self.z)**2
        )
        return distance < self.r








sphere1 = Sphere(5, 1, 2, 3)
sphere2 = Sphere(2)


print(f"Объем первой сферы: {sphere1.get_volume()}")
print(f"Площадь поверхности первой сферы: {sphere1.get_square()}")


sphere2.set_radius(3)
sphere2.set_center(10, 5, 6)


print(f"Точка (4, 5, 7) внутри второй сферы: {sphere2.is_point_inside(4, 5, 7)}")



