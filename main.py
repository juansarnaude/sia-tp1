import sys

from algorithms.bfs import bfs
from algorithms.dfs import dfs
from models.Map import Map
from models.State import State


with open(f"{sys.argv[1]}", "r") as file:
    map = Map(file) # We load the map when creating the instance
    initial_state = State(map.player_start, map.boxes)
    last_node, solution_path = bfs(initial_state, map)

if solution_path:
    # print("Solution found:")
    # for step in solution_path:
    #     print(f"Move: {step.action}, State: {step.state}")
    print(last_node)
else:
    print("No solution found.")

