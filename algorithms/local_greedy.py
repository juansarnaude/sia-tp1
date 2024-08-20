from asyncio import PriorityQueue

from models.Direction import Direction
from models.Node import Node


def local_greedy(initial_state, map, heuristics):
    explored = set()

    current_node = Node(initial_state).set_cost(0)
    root_node=current_node
    heuristics.apply(current_node)

    while current_node:

        if current_node.state.is_goal_state(map):
            return current_node, len(explored), 0

        explored.add(current_node.state)

        min_cost = float('inf')
        best_node = None
        min_state = None

        for direction in Direction:
            child_state = current_node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, current_node, direction, cost=0)

                heuristics.apply(new_node)

                if new_node.cost < min_cost:
                    min_state = child_state
                    min_cost = new_node.cost
                    best_node = new_node

        if best_node:
            current_node = best_node
            explored.add(min_state)
        elif current_node==root_node:
            return None
        else:
            #backtracking
            current_node = current_node.parent

