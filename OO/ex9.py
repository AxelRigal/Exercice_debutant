class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Cube(Shape):
    def __init__(self, z=0):
        super().__init__()
        self.z = z

cube = Cube()
print(cube.x)
print(cube.y)
print(cube.z)
