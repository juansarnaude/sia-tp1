import itertools
import math

from heuristics.box_stuck import MapWithMarkedStuckPoints


def manhattan(node = None, map = None):
    if map:
        manhattan.map = map

    else:
        distances = []
        for box_instance in node.state.boxes:
            box_instance_distances = []
            for goal in manhattan.map.goals:
                box_instance_distance = math.fabs(box_instance.x- goal.x) + math.fabs(box_instance.y - goal.y)
                box_instance_distance += abs(node.state.player.x- box_instance.x) + abs(node.state.player.y - box_instance.y)
                box_instance_distances.append(box_instance_distance)

            distances.append(box_instance_distances)


        # Check of the combiation of box->goals that minimizes distances
        min_cost = float('inf')
        for box_goals_distances in itertools.permutations(range(len(distances)), len(distances)):
            min_cost = min(sum(distances[box][goal] for box,goal in enumerate(box_goals_distances)), min_cost)

        node.add_cost(min_cost)




