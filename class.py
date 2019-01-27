class Point:
    x = 0
    y = 0

    @classmethod
    def ones(cls):
        return cls(1, 1)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left_in_x_coordinate(self, units):
        self.x -= units

    def move_right_in_x_coordinate(self, units):
        self.x += units

    def move_right_in_y_coordinate(self, units):
        self.y += units

    def move_left_in_y_coordinate(self, units):
        self.y -= units

    def print_coordinates(self):
        print(f"x: {self.x} , y: {self.y}")


point1 = Point.ones()
point1.move_left_in_x_coordinate(-3)
point1.move_left_in_y_coordinate(-3)
point1.move_right_in_x_coordinate(0)
point1.move_right_in_y_coordinate(0)
point1.print_coordinates()


class bird:
    def __init__(self, x):
        self.isFlying = x

    @classmethod
    def zero(cls):
        return cls(0)

    def fly(self):
        self.isFlying = 1
        return

    def land(self):
        self.isFlying = 0
        return 1


penguin = bird.zero()
penguin.fly()


parrot = bird.zero()
parrot.fly()
if parrot.isFlying:
    print(f"parrot is flying with corrosponding value of {parrot.isFlying}")
else:
    print("parrot is landing")
