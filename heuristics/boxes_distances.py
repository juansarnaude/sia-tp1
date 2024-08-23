import itertools
import math

from heuristics.box_stuck import MapWithMarkedStuckPoints


def boxes_distances(node = None, map = None):
    if map:
        boxes_distances.map = map

    else:
        distances = []
        # Similar to manhattan but also contemplating the distance the player has to the boxes.
        # Another difference is that it stores every results instead of returning the minimum
        for box_instance in node.state.boxes:
            box_instance_distances = []
            for goal in boxes_distances.map.goals:
                box_instance_distance = math.fabs(box_instance.x- goal.x) + math.fabs(box_instance.y - goal.y)
                box_instance_distance += abs(node.state.player.x- box_instance.x) + abs(node.state.player.y - box_instance.y)
                box_instance_distances.append(box_instance_distance)

            distances.append(box_instance_distances)


        # Check of the combiation of box->goals that minimizes distances
        min_cost = float('inf')
        for box_goals_distances in itertools.permutations(range(len(distances)), len(distances)):
            min_cost = min(sum(distances[box][goal] for box,goal in enumerate(box_goals_distances)), min_cost)

        node.add_cost(min_cost)




