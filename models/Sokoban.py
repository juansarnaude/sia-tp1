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
        self.boxes_placed = 0
        self.boxes_needed = 0


    def __eq__(self, other):
        if not isinstance(other, Sokoban):
            return False
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.player, frozenset(self.boxes)))

    def init_player(self, x, y):
        self.player.__set_coords__(x, y)
        self.map[y][x] = '@'

    def add_wall(self, x, y):
        self.walls.add(Coordinates(x,y))
        self.map[y][x] = '#'

    def add_flag(self, x, y):
        self.flags.add(Coordinates(x,y))
        self.map[y][x] = '.'
        self.boxes_needed = min(len(self.flags), len(self.boxes))

    def add_box(self, x, y):
        self.boxes.add(Coordinates(x,y))
        self.map[y][x] = '$'
        self.boxes_needed = min(len(self.flags), len(self.boxes))

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

            #Changes position of box and its instance
            self.boxes.discard(Coordinates(new_x,new_y))
            self.boxes.add(Coordinates(box_new_x,box_new_y))
            if self.map[new_y][new_x] == '.':
                self.check_win(-1)
            if self.map[box_new_y][box_new_x] == '.':
                self.check_win(1)
            self.map[box_new_y][box_new_x] = '$'

        if Coordinates(self.player.x, self.player.y) in self.flags:
            self.map[self.player.y][self.player.x] = '.'
        else:
            self.map[self.player.y][self.player.x] = ' '

        self.player.move(step_x, step_y)
        self.map[self.player.y][self.player.x] = '@'

    def check_win(self, to_add):
        self.boxes_placed = self.boxes_placed + to_add
        if self.boxes_needed == self.boxes_placed:
            print('WIN')
            exit(0)


    def display_map(self):
        for row in self.map:
            print(''.join(row))