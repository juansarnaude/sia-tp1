import sys
import json
import time
from datetime import datetime

from algorithms.a_star import a_star
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from heuristics.box_stuck import box_stuck
from heuristics.heuristic import Heuristic
from models.Map import Map
from models.State import State
from models.Node import Node


with open(f"{sys.argv[1]}", "r") as file:
    sokoban_map = Map(file) # We load the map when creating the instance
    initial_state = State(sokoban_map.player_start, sokoban_map.boxes)
    data = {}

    with open(f"configs/config.json", 'r') as config_file:
        config = json.load(config_file)

        if config["report"] == "full":
            start_time = time.time()


        if config["algorithm"] == "bfs":
            last_node, explored_nodes_count, frontier_node_counts = bfs(initial_state, sokoban_map)
        elif config["algorithm"] == "dfs":
            last_node, explored_nodes_count, frontier_node_counts = bfs(initial_state, sokoban_map)
        elif config["algorithm"] == "a_star":
            heuristic = Heuristic(config["heuristics"], sokoban_map)
            last_node, explored_nodes_count, frontier_node_counts = a_star(initial_state, sokoban_map, heuristic)


        if config["report"] == "full" and last_node:
            end_time = time.time()
            elapsed_time = end_time - start_time
            data["initial_map"] = sokoban_map.print_grid()
            data["result"] = "success"
            data["execution_time"] = f"elapsed_time: {elapsed_time:.5f} s"
            data["explored_nodes_count"] = explored_nodes_count
            data["frontier_node_counts"] = frontier_node_counts

        if last_node:
            data["solution"] = f"{last_node}"

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

        with open(f"results/result{formatted_time}.json", 'w') as result_file:
            json.dump(data, result_file, indent=5)

