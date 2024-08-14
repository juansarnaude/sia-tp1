from models.Sokoban import Sokoban

def read_sokoban_level(file):
    sokoban_map = file.readlines()
    sokoban = Sokoban()

    for i, line in enumerate(sokoban_map):
        new_row = []
        for j, char in enumerate(line.rstrip()):
            if char == '#':
                sokoban.add_wall(j, i)
            elif char == '.':
                sokoban.add_flag(j, i)
            elif char == '$':
                sokoban.add_box(j, i)
            elif char == '@':
                sokoban.init_player(j, i)

    return sokoban