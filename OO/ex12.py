class Cube:
<<<<<<< HEAD
    def __init__(x=5, y=2, z=7):
        x = x
        y = y
        z = z

    def move_x():
        x += 1
=======
    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def move_x(self):
        self.x += 1
>>>>>>> 008bf3ea56fe7b905ccf33117a93190016ccd0ae


mon_cube = Cube()
mon_cube.move_x()
<<<<<<< HEAD
=======
# print(*mon_cube)
print(mon_cube.x)
print(mon_cube.y)
print(mon_cube.z)
>>>>>>> 008bf3ea56fe7b905ccf33117a93190016ccd0ae
