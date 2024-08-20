from heuristics.box_stuck import box_stuck
from heuristics.boxes_in_goals import boxes_in_goals
from heuristics.euclidean import euclidean


class Heuristic:
    def __init__(self, heuristics_list, map):
        self.box_stuck, self.boxes_in_goals, self.euclidean = None, None, None

        if "box_stuck" in heuristics_list:
            self.box_stuck = 1
            box_stuck(map= map)

        if "boxes_in_goals" in heuristics_list:
            self.boxes_in_goals = 1
            boxes_in_goals(map= map)

        if "euclidean" in heuristics_list:
            self.euclidean = 1
            euclidean(map=map)

    def apply(self, node):
        if self.box_stuck:
            box_stuck(node=node)
        if self.boxes_in_goals:
            boxes_in_goals(node=node)
        if self.euclidean:
            euclidean(node=node)

