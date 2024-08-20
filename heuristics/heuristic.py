from heuristics.box_stuck import box_stuck


class Heuristic:
    def __init__(self, heuristics_list, map):
        if heuristics_list.contains("box_stuck"):
            self.box_stuck = 1
            box_stuck(map= map)

    def apply(self, node):
        if self.box_stuck:
            box_stuck(node=node)

