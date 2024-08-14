from models.Coordinates import Coordinates
from models.Direction import Direction, get_direction_value

class Sokoban:
    def __init__(self):
        self.walls = set()
        self.flags = set()
        self.boxes = set()
        self.player = Coordinates(-1,-1)
        self.boxes_placed = 0
        self.boxes_needed = 0
        self.steps = 0

    def change_state(self, steps, boxes, player):
        self.steps = steps
        self.boxes = boxes
        self.player = player

    def get_state(self):
        return self.steps, self.boxes, self.player

    def __eq__(self, other):
        if not isinstance(other, Sokoban):
            return False
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.player, frozenset(self.boxes)))

    def init_player(self, x, y):
        self.player.__set_coords__(x, y)

    def add_wall(self, x, y):
        self.walls.add(Coordinates(x,y))

    def add_flag(self, x, y):
        self.flags.add(Coordinates(x,y))
        self.boxes_needed = min(len(self.flags), len(self.boxes))

    def add_box(self, x, y):
        self.boxes.add(Coordinates(x,y))
        self.boxes_needed = min(len(self.flags), len(self.boxes))

    #VERTICAL COORDINATES ARE OPPOSITE OF WHAT WE USUALLY USE SO
    #UP IS +(0,-1), DOWN IS +(1,0)
    def move(self, direction):
        (step_x, step_y) = get_direction_value(direction)
        new_x = self.player.x + step_x
        new_y = self.player.y + step_y

        if Coordinates(new_x, new_y) in self.walls:
            return

        if Coordinates(new_x, new_y) in self.boxes:
            box_new_x = new_x + step_x
            box_new_y = new_y + step_y

            if Coordinates(box_new_x, box_new_y) in self.walls or Coordinates(box_new_x, box_new_y) in self.boxes:
                return

            #Changes position of box and its instance
            self.boxes.discard(Coordinates(new_x,new_y))
            self.boxes.add(Coordinates(box_new_x,box_new_y))
            if Coordinates(new_x, new_y) in self.flags:
                self.check_win(-1)
            if Coordinates(box_new_x, box_new_y) in self.flags:
                self.check_win(1)

        self.player.move(step_x, step_y)

    def check_win(self, to_add):
        self.boxes_placed = self.boxes_placed + to_add
        print(self.boxes_placed , self.boxes_needed)
        if self.boxes_needed == self.boxes_placed:
            print('WIN')


    def display_map(self):
        width = max(coord.x for coord in self.walls)+1
        height = max(coord.y for coord in self.walls)+1

        print("Now printing map")

        map_grid = [[' ' for _ in range(width)] for _ in range(height)]

        for walls_coord in self.walls:
            map_grid[walls_coord.y][walls_coord.x] = '#'
        for flags_coord in self.flags:
            map_grid[flags_coord.y][flags_coord.x] = '.'
        for box_coord in self.boxes:
            map_grid[box_coord.y][box_coord.x] = '$'
        map_grid[self.player.y][self.player.x] = '@'

        for row in map_grid:
            print(''.join(row))
