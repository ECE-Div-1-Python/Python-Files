class Solid:
    def __init__(self, p):
        self.p = p

    def surface_area(self):
        return None

    def volume(self):
        return None


class Cube(Solid):
    def surface_area(self):
        side = self.p['side']
        return 6 * (side ** 2)

    def volume(self):
        return self.p["side"] ** 3


class Sphere(Solid):
    def surface_area(self):
        r = self.p["radius"]
        return float(4 * 3.14 * r * r)

    def volume(self):
        return float((4 / 3) * 3.14 * self.p["radius"] ** 3)



cube = Cube({'side': 5})
print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())

sphere = Sphere({'radius': 3})
print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())


