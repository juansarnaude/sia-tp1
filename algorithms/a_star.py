from queue import PriorityQueue

from heuristics.box_stuck import box_stuck
from models.Direction import Direction
from models.Node import Node


def a_star(initial_state, map, heuristic):
    frontier = PriorityQueue()
    explored = set()

    node = Node(initial_state).set_cost(0)
    heuristic.apply(node)
    frontier.put((node.cost, node))


    while frontier:
        _, node = frontier.get()

        if node.state.is_goal_state(map):
            return node, len(explored), frontier.qsize()

        explored.add(node.state)

        for direction in Direction:
            child_state = node.state.move(direction, map)
            if child_state and child_state not in explored:
                # G(n)
                new_node = Node(child_state, node, direction, cost=node.cost+1)
                # H(n)
                heuristic.apply(new_node)
                frontier.put((new_node.cost, new_node))

    return None