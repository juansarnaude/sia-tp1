from queue import PriorityQueue

from heuristics.heuristic import Heuristic
from models.Map import Map
from models.Direction import Direction
from models.Node import Node
from models.State import State


def a_star(initial_state: State, game_map: Map, heuristic: Heuristic):
    frontier = PriorityQueue()
    explored = set()

    # Crea el nodo inicial
    start_node = Node(initial_state, cost=0)
    # Aplica la heurística inicial
    heuristic.apply(start_node)

    # Agrega el nodo inicial a la frontera
    frontier.put((start_node.cost, start_node))

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node.state.is_goal_state(game_map):
            return current_node, len(explored), frontier.qsize()

        explored.add(current_node.state)

        for direction in Direction:
            child_state = current_node.state.move(direction, game_map)
            if child_state and child_state not in explored:
                # Crea el nodo hijo
                child_node = Node(child_state, parent=current_node, action=direction, cost=current_node.cost + 1)
                # Aplica la función heurística
                heuristic.apply(child_node)
                # Agrega el nodo hijo a la frontera
                frontier.put((child_node.cost, child_node))

    return None, len(explored), frontier.qsize()
