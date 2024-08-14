from models.Coordinates import Coordinates
from models.Direction import Direction, get_direction_value


class Sokoban:
    def __init__(self, width, height):
        self.map = [[' ' for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

        self.walls = set()
        self.flags = set()
        self.boxes = set()
        self.player = Coordinates(-1,-1)

    def init_player(self, x, y):
        self.player.__set_coords__(x, y)
        self.map[y][x] = '@'

    def add_wall(self, x, y):
        self.walls.add(Coordinates(x,y))
        self.map[y][x] = '#'

    def add_flag(self, x, y):
        self.flags.add(Coordinates(x,y))
        self.map[y][x] = '.'

    def add_box(self, x, y):
        self.boxes.add(Coordinates(x,y))
        self.map[y][x] = '$'


    #VERTICAL COORDINATES ARE OPPOSITE OF WHAT WE USUALLY USE SO
    #UP IS +(0,-1), DOWN IS +(1,0)
    def move(self, direction):
        (step_x, step_y) = get_direction_value(direction)

        new_x = self.player.x + step_x
        new_y = self.player.y + step_y


        if self.map[new_y][new_x] == '#':
            return

        if self.map[new_y][new_x] == '$':
            box_new_x = new_x + step_x
            box_new_y = new_y + step_y

            if self.map[box_new_y][box_new_x] == '#' or self.map[box_new_y][box_new_x] == '$':
                return

            self.map[box_new_y][box_new_x] = '$'
            self.map[new_y][new_x] = ' '

        self.map[self.player.y][self.player.x] = ' '
        self.player.move(step_x, step_y)
        self.map[self.player.y][self.player.x] = '@'


    def display_map(self):
        for row in self.map:
            print(''.join(row))