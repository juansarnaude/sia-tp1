#this file is for setting parameters in configs/config.json an running a specific setup

import sys
import json
import time
from datetime import datetime

from algorithms.a_star import a_star
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.local_greedy import local_greedy
from algorithms.global_greedy import global_greedy
from algorithms.iddfs import iddfs
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

        results_list = []
        explored_nodes_count_list =[]
        frontier_node_counts_list = []
        execution_time_list= []
        solutions_list = []
        solution_length_list = []
        iddfs_limit_list=[]

        iteration_count = config["iteration_count"]

        for i in range(iteration_count):
            start_time = time.time()

            if config["algorithm"] == "bfs":
                last_node, explored_nodes_count, frontier_node_counts = bfs(initial_state, sokoban_map)
            elif config["algorithm"] == "dfs":
                last_node, explored_nodes_count, frontier_node_counts = dfs(initial_state, sokoban_map)
            elif config["algorithm"] == "iddfs":
                iddfs_limit=1 if config["iddfs_limit"]<0 else config["iddfs_limit"]
                last_node, explored_nodes_count, frontier_node_counts = iddfs(initial_state, sokoban_map,iddfs_limit)
                iddfs_limit_list.append(iddfs_limit)
            elif config["algorithm"] == "a_star":
                heuristic = Heuristic(config["heuristics"], sokoban_map)
                last_node, explored_nodes_count, frontier_node_counts = a_star(initial_state, sokoban_map, heuristic)
            elif config["algorithm"] == "local_greedy":
                heuristic = Heuristic(config["heuristics"], sokoban_map)
                last_node, explored_nodes_count, frontier_node_counts = local_greedy(initial_state, sokoban_map, heuristic)
            elif config["algorithm"] == "global_greedy":
                heuristic = Heuristic(config["heuristics"], sokoban_map)
                last_node, explored_nodes_count, frontier_node_counts = global_greedy(initial_state, sokoban_map, heuristic)

            end_time = time.time()
            elapsed_time = end_time - start_time
            execution_time_list.append(elapsed_time)

            explored_nodes_count_list.append(explored_nodes_count)
            frontier_node_counts_list.append(frontier_node_counts)

            if last_node:
                node = last_node
                sol_str = ''
                while node:
                    sol_str = node.__repr__() + sol_str
                    node = node.parent
                solutions_list.append(sol_str)
                solution_length_list.append(len(sol_str))

            # We reset heuristic so we dont give an advantage to heuristics that take a huge amount of time setting
            heuristic = None


        if last_node:
            data["status"]="success"
            data["solution"] = solutions_list
            data["solution_length"] = solution_length_list
        else:
            data["status"]="failure"
        if len(iddfs_limit_list)>0:
            data["iddfs_limit"]=iddfs_limit_list
        data["execution_time"] = execution_time_list
        data["explored_nodes_count"] = explored_nodes_count_list
        data["frontier_node_counts"] = frontier_node_counts_list
        data["initial_map"] = sokoban_map.print_grid()
        data["algorithm"] = config["algorithm"]
        data["heuristic"] = config["heuristics"]

        output_file_name = ""

        if config["output_file_name"] == "":
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
            level = f"{sys.argv[1]}".split("/")[-1]
            output_file_name = f"result_"f"{level}_{formatted_time}"
        else:
            output_file_name = config["output_file_name"]


        with open(output_file_name, 'w') as result_file:
            json.dump(data, result_file, indent=5)

