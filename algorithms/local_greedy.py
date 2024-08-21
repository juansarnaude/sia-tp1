import bisect
from queue import PriorityQueue
from collections import deque
from models.Node import Node
from models.Direction import Direction
from models.State import State


def local_greedy(initial_state, map, heuristic):
    frontier = PriorityQueue()
    explored = set()

    node = Node(initial_state, depth=0)
    heuristic.apply(node)
    frontier.put((node.depth, node))


    while frontier:
        _, node = frontier.get()

        #print(node.depth)

        # Check if we have reached the goal state
        if node.state.is_goal_state(map):
            return node, len(explored), frontier.qsize()

        explored.add(node.state)

        # Explore neighbors
        for direction in Direction:
            child_state = node.state.move(direction, map)
            if child_state and child_state not in explored:
                new_node = Node(child_state, node, direction, depth=node.depth+1)
                heuristic.apply(new_node)
                frontier.put(( -new_node.depth , new_node))

    # Return None if no solution is found
    return None
