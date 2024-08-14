import sys

from models.Direction import Direction
from read_sokoban_level import read_sokoban_level


def test_equals():
    with open(f"{sys.argv[1]}", "r") as file:
        sokoban1 = read_sokoban_level(file)
        sokoban1.move(Direction.RIGHT)
        sokoban1.display_map()

    print("--------------------")

    with open(f"{sys.argv[2]}", "r") as file:
        sokoban2 = read_sokoban_level(file)
        sokoban2.move(Direction.RIGHT)
        sokoban2.move(Direction.DOWN)
        sokoban2.display_map()

    print("--------------------")

    print(sokoban1.__eq__(sokoban2))

def test_movement():
    with open(f"{sys.argv[1]}", "r") as file:
        sokoban = read_sokoban_level(file)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.UP)
        sokoban.move(Direction.UP)
        sokoban.move(Direction.UP)
        sokoban.move(Direction.UP)
        sokoban.display_map()


def test_win():
    with open(f"{sys.argv[1]}", "r") as file:
        sokoban = read_sokoban_level(file)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.move(Direction.RIGHT)
        sokoban.display_map()
