from models.Coordinates import Coordinates

class Map:
    def __init__(self, file):
        self.grid = []
        self.player_start = None
        self.goals = set()
        self.boxes = set()

        self.load_map(file)

    def load_map(self, file):
        for y, line in enumerate(file):
            row = []
            for x, char in enumerate(line.rstrip()):
                row.append(char)
                if char == '@':
                    self.player_start = Coordinates(x, y)
                elif char == '.':
                    self.goals.add(Coordinates(x, y))
                elif char == '$':
                    self.boxes.add(Coordinates(x, y))
                elif char == '*':
                    self.boxes.add(Coordinates(x, y))
                    self.goals.add(Coordinates(x, y))
                elif char == '+':
                    self.goals.add(Coordinates(x, y))
                    self.player_start = Coordinates(x, y)
            self.grid.append(row)

    def is_wall(self, coord):
        return self.grid[coord.y][coord.x] == '#'

    def is_goal(self, coord):
        return coord in self.goals

    def is_box(self, coord):
        return coord in self.boxes

    def __repr__(self):
        return f"Map(player_start={self.player_start}, goals={self.goals}, boxes={self.boxes})"
