import sys
from read_sokoban_level import read_sokoban_level
from models.Sokoban import Sokoban
from models.Direction import Direction

with open(f"{sys.argv[1]}", "r") as file:
    sokoban = read_sokoban_level(file)
    sokoban.move(Direction.RIGHT)
    sokoban.display_map()



