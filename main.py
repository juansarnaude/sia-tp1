import sys
from read_sokoban_level import read_sokoban_level
from models.Sokoban import Sokoban


with open(f"{sys.argv[1]}", "r") as file:
    sokoban = read_sokoban_level(file)
    sokoban.move('u')
    sokoban.move('d')
    sokoban.move('r')
    sokoban.display_map()



