class Road:
    _mass = 25

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        print("Mass of road = ", self.width * self.length * self.height * self._mass)


length = float(input("Enter length:\n"))
width = float(input("Enter width:\n"))
height = float(input("Enter height:\n"))
road = Road(width, length, height)
