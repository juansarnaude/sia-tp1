import math

import numpy as np
from models.Node import Node
from models.Map import Map

def euclidean_non_admissible(node: Node = None, map: Map = None) -> float:
    if map:
        euclidean_non_admissible.map = map
        return
    else:
        distances = 0
        for box in node.state.boxes:
            shortest_distance = float('inf')
            for goal in euclidean_non_admissible.map.goals:
                distance = box.distance_to(goal)
                if distance < shortest_distance:
                    shortest_distance = distance
            distances+=shortest_distance
        node.add_cost(distances)
        return