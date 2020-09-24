class Cube:
    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def move_x(self):
        self.x += 1


mon_cube = Cube()
mon_cube.move_x()
# print(*mon_cube)
print(mon_cube.x)
print(mon_cube.y)
print(mon_cube.z)
