#this file is for generating a dataset and comparing different informed search algorithms with different heuristics
import json
import time

from algorithms.a_star import a_star
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.local_greedy import local_greedy
from algorithms.global_greedy import global_greedy
from algorithms.iddfs import iddfs
from heuristics.heuristic import Heuristic
from models.Map import Map
from models.State import State

def sokoban(algorithm, heuristics, map_file_name, output_file_name,iteration_count,iddfs_limit=1):
    with open(map_file_name, "r") as file:
        sokoban_map = Map(file) # We load the map when creating the instance
        initial_state = State(sokoban_map.player_start, sokoban_map.boxes)
        data = {}

        explored_nodes_count_list =[]
        frontier_node_counts_list = []
        execution_time_list= []
        solutions_list = []
        solution_length_list = []
        iddfs_limit_list=[]


        for i in range(iteration_count):
            start_time = time.time()
            if algorithm == "bfs":
                last_node, explored_nodes_count, frontier_node_counts = bfs(initial_state, sokoban_map)
            elif algorithm == "dfs":
                last_node, explored_nodes_count, frontier_node_counts = dfs(initial_state, sokoban_map)
            elif algorithm == "iddfs":
                iddfs_limit=1 if iddfs_limit<0 else iddfs_limit
                last_node, explored_nodes_count, frontier_node_counts = iddfs(initial_state, sokoban_map,iddfs_limit)
                iddfs_limit_list.append(iddfs_limit)
            elif algorithm == "a_star":
                heuristic = Heuristic(heuristics, sokoban_map)
                last_node, explored_nodes_count, frontier_node_counts = a_star(initial_state, sokoban_map, heuristic)
            elif algorithm == "local_greedy":
                heuristic = Heuristic(heuristics, sokoban_map)
                last_node, explored_nodes_count, frontier_node_counts = local_greedy(initial_state, sokoban_map, heuristic)
            elif algorithm == "global_greedy":
                heuristic = Heuristic(heuristics, sokoban_map)
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
                data["status"] = "success"
                data["solution"] = solutions_list
                data["solution_length"] = solution_length_list
            else:
                data["status"] = "failure"
            if len(iddfs_limit_list) > 0:
                data["iddfs_limit"] = iddfs_limit_list
            data["execution_time"] = execution_time_list
            data["explored_nodes_count"] = explored_nodes_count_list
            data["frontier_node_counts"] = frontier_node_counts_list
            data["initial_map"] = sokoban_map.print_grid()
            data["algorithm"] = algorithm
            data["heuristic"] = heuristics

            with open(output_file_name, 'w') as result_file:
                json.dump(data, result_file, indent=5)

