import numpy as np
from models.Direction import Direction

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Coordinates(x={self.x}, y={self.y})"

    def move(self, direction):
        if direction == Direction.UP:
            return Coordinates(self.x, self.y - 1)
        elif direction == Direction.DOWN:
            return Coordinates(self.x, self.y + 1)
        elif direction == Direction.LEFT:
            return Coordinates(self.x - 1, self.y)
        elif direction == Direction.RIGHT:
            return Coordinates(self.x + 1, self.y)
        return self
    
    def to_array(self):
        return [self.x, self.y]
    
    def distance_to(self, other: 'Coordinates') -> float:
        return np.linalg.norm(np.array(self.to_array()) - np.array(other.to_array()))


