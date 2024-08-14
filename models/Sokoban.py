from models.Coordinates import Coordinates

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
        #UP
        if direction == 'u':
            if self.map[self.player.y][self.player.x-1] == '#':
                return
            self.map[self.player.y][self.player.x] = ' '
            self.player.move(0, -1)
            self.map[self.player.y][self.player.x] = '@'


        #DOWN
        elif direction == 'd':
            if self.map[self.player.y][self.player.x-1] == '#':
                return
            self.map[self.player.y][self.player.x] = ' '
            self.player.move(0, 1)
            self.map[self.player.y][self.player.x] = '@'


        #RIGHT
        elif direction == 'r':
            if self.map[self.player.y+1][self.player.x] == '#':
                return
            self.map[self.player.y][self.player.x] = ' '
            self.player.move(1, 0)
            self.map[self.player.y][self.player.x] = '@'


        #LEFT
        elif direction == 'l':
            if self.map[self.player.y-1][self.player.x] == '#':
                return
            self.map[self.player.y][self.player.x] = ' '
            self.player.move(-1, 0)
            self.map[self.player.y][self.player.x] = '@'

        else:
            return


    def display_map(self):
        for row in self.map:
            print(''.join(row))