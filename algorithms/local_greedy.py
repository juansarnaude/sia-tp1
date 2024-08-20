from asyncio import PriorityQueue

from models.Direction import Direction
from models.Node import Node


def local_greedy(initial_state, map, heuristics):
    explored = set()
    current_node = Node(initial_state).set_cost(0)
    root_node = current_node
    heuristics.apply(current_node)

    explored.add(current_node.state)

    while current_node:
        if current_node.state.is_goal_state(map):
            print("OOOSSSAAA")
            print(current_node.cost)
            print(len(explored))
            return current_node, len(explored), 0



        min_cost = float('inf')
        best_node = None

        for direction in Direction:
            child_state = current_node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, current_node, direction, cost=current_node.cost + 1)
                heuristics.apply(new_node)

                # Compare the cost of the next states locally
                if new_node.cost < min_cost:
                    min_cost = new_node.cost
                    best_node = new_node

        # Check if best node exist
        if best_node:
            current_node = best_node
            explored.add(current_node.state)
        else:
            #Backtrack
            if current_node!=root_node:
                current_node = current_node.parent

    return None