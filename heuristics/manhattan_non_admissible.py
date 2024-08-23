import math

import numpy as np

from models.Map import Map
from models.Node import Node


def manhattan_non_admissible(node: Node = None, map: Map = None) -> float:
    if map:
        manhattan_non_admissible.map = map
        return
    else:
        distances = []
        for box in node.state.boxes:
            shortest_distance = float('inf')
            for goal in manhattan_non_admissible.map.goals:
                distance = math.fabs(box.x- goal.x) + math.fabs(box.y - goal.y)
                if distance < shortest_distance:
                    shortest_distance = distance
            distances.append(shortest_distance)
        node.add_cost(np.array(distances).sum())
        return