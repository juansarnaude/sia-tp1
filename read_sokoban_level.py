from models.Coordinates import Coordinates
from models.Sokoban import  SokobanState, SokobanMap


def read_sokoban_level(file):
    level_file = file.readlines()
    sokoban_map = SokobanMap()

    boxes = set()
    player = Coordinates(-1,-1)

    for i, line in enumerate(level_file):
        new_row = []
        for j, char in enumerate(line.rstrip()):
            if char == '#':
                sokoban_map.add_wall(j, i)
            elif char == '.':
                sokoban_map.add_flag(j, i)
            elif char == '$':
                boxes.add(Coordinates(j, i))
            elif char == '@':
                player = Coordinates(j, i)

    sokoban_state = SokobanState('', boxes, player)

    return sokoban_map, sokoban_state