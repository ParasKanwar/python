class bird:

    # magic methods below

   # magic method for initializing object with some values

    def __init__(self, x):
        self.isFlying = x

   # magic method for object identity

    def __str__(self):
        if self.isFlying == 0:
            return f"bird is not flying {self.isFlying}"
        else:
            return f"bird is flying with rate of {self.isFlying}"

    # magic method for determing object comparisions

    def __eq__(self, other):
        return self.isFlying == other.isFlying

    def __gt__(self, other):
        return self.isFlying > other.isFlying

    def __lt__(self, other):
        return self.isFlying < other.isFlying

    # magic methods for arthematic operations between objects
    def __add__(self, other):
        return bird(self.isFlying + other.isFlying)

    # class methos below

    @classmethod
    def flying(cls, rate):
        return cls(rate)

    @classmethod
    def not_flying(cls):
        return cls(0)

    # instance level methods

    def fly(self):
        self.isFlying = 1
        return self.isFlying

    def land(self):
        self.isFlying = 0
        return self.isFlying


bird1 = bird(3)
bird2 = bird(5)
bird3 = bird1+bird2
print(bird3.isFlying)
