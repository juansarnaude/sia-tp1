import time
import copy
from asyncio import PriorityQueue

from models.Direction import Direction
from models.Node import Node


def local_greedy(initial_state, map, heuristics):
    explored = set()
    current_node = Node(initial_state)
    root_node = current_node
    heuristics.apply(current_node)

    explored.add(current_node.state)

    while current_node:
        if current_node.state.is_goal_state(map):
            return current_node, len(explored), 0

        min_cost = float('inf')
        best_node = None

        for direction in Direction:
            child_state = current_node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, current_node, direction)
                heuristics.apply(new_node)
                print(f"new node cost is {new_node.cost}")

                # Compare the cost of the next states locally
                if new_node.cost < min_cost:
                    min_cost = new_node.cost
                    best_node = new_node

        # Check if best node exist
        if best_node:
            current_node = copy.deepcopy(best_node)
        else:
            #Backtrack
            if current_node!=root_node:
                current_node = copy.deepcopy(current_node.parent)
            else: return None

        explored.add(current_node.state)

    return None