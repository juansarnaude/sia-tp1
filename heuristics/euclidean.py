import math

import numpy as np
from models.Node import Node
from models.Map import Map

def euclidean(node: Node = None, map: Map = None) -> float:
    if map:
        euclidean.map = map
        return
    else:
        distances = 0
        for box in node.state.boxes:
            shortest_distance = float('inf')
            player_to_box_distance = node.state.player.distance_to(box)
            for goal in euclidean.map.goals:
                distance = box.distance_to(goal) + player_to_box_distance
                if distance < shortest_distance:
                    shortest_distance = distance
            distances+=shortest_distance
        node.add_cost(distances)
        return