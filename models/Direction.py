from enum import Enum

class Direction(Enum):
    UP = 'u'
    DOWN = 'd'
    RIGHT = 'r'
    LEFT = 'l'

def get_direction_value(value):
    if value == Direction.UP:
        return  0, -1
    if value == Direction.DOWN:
        return 0, 1
    if value == Direction.RIGHT:
        return 1, 0
    if value == Direction.LEFT:
        return -1, 0
