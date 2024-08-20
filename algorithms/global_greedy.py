from queue import PriorityQueue

from models.Direction import Direction
from models.Node import Node


def global_greedy(initial_state, map, heuristics):
    frontier = PriorityQueue()
    explored = set()

    node = Node(initial_state).set_cost(0)
    heuristics.apply(node)
    frontier.put((node.cost, node))

    # We use bfs

    while frontier:
        _, node = frontier.get()

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
            return node, len(explored), frontier.qsize()

        explored.add(node.state)

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, node, direction)
                heuristics.apply(new_node)
                frontier.put((new_node.cost, new_node))

    # Return None if no solution is found
    return None
