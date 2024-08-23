from heuristics.box_stuck import box_stuck
from heuristics.manhattan import manhattan
from heuristics.boxes_in_goals import boxes_in_goals
from heuristics.euclidean import euclidean
from heuristics.manhattan_non_admissible import manhattan_non_admissible
from heuristics.euclidean_non_admissible import euclidean_non_admissible

class Heuristic:
    def __init__(self, heuristics_list, map):
        self.box_stuck = None
        self.boxes_in_goals = None
        self.euclidean = None
        self.manhattan = None
        self.manhattan_non_admissible = None
        self.euclidean_non_admissible = None

        self.map = map  # Guarda el mapa para su uso en la heurística

        if "box_stuck" in heuristics_list:
            self.box_stuck = 1
            box_stuck(map=map)

        if "boxes_in_goals" in heuristics_list:
            self.boxes_in_goals = 1
            boxes_in_goals(map=map)

        if "euclidean" in heuristics_list:
            self.euclidean = 1
            euclidean(map=map)

        if "manhattan" in heuristics_list:
            self.manhattan = 1
            manhattan(map=map)

        if "manhattan_non_admissible" in heuristics_list:
            self.manhattan_non_admissible = 1
            manhattan_non_admissible(map=map)

        if "euclidean_non_admissible" in heuristics_list:
            self.euclidean_non_admissible = 1
            euclidean_non_admissible(map=map)

    def apply(self, node):
        if self.box_stuck:
            box_stuck(node=node)
        if self.boxes_in_goals:
            boxes_in_goals(node=node)
        if self.euclidean:
            euclidean(node=node)
        if self.manhattan:
            manhattan(node=node)  # Pasa el mapa junto con el nodo
        if self.manhattan_non_admissible:
            manhattan_non_admissible(node=node)
        if self.euclidean_non_admissible:
            euclidean_non_admissible(node=node)

