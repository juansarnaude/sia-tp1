import sys

from algorithms.dfs import dfs
from algorithms.bfs import bfs
from read_sokoban_level import read_sokoban_level
from models.Direction import Direction
from tests import test_equals, test_movement, test_win, test_play_game


with open(f"{sys.argv[1]}", "r") as file:
    sokoban_map, sokoban_state = read_sokoban_level(file)
    bfs(sokoban_map, sokoban_state)
