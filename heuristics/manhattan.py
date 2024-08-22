import numpy as np

from models.Map import Map
from models.Node import Node


def manhattan(node: Node = None, map: Map = None) -> float:
    if not hasattr(manhattan, "map"):
        manhattan.map = map
        return
    else:
        distances = []
        for box in node.state.boxes:
            shortest_distance = float('inf')
            for goal in manhattan.map.goals:
                distance = box.distance_to(goal)
                if distance < shortest_distance:
                    shortest_distance = distance
            distances.append(shortest_distance)
        node.add_cost(np.array(distances).sum())
        return