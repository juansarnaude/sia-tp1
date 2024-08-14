class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __set_coords__(self, x, y):
        self.x = x
        self.y = y

    def __set_x__(self, x):
        self.x = x

    def __set_y__(self, y):
        self.y = y

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y


    def x(self):
        return self.x

    def y(self):
        return self.y

