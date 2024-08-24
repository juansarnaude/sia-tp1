import math


def manhattan(node=None, map=None):
    if map:
        manhattan.map = map
    else:
        total_manhattan_distance = 0
        for box_instance in node.state.boxes:
            player_distance = math.fabs(box_instance.x - node.state.player.x) + math.fabs(box_instance.y -  node.state.player.y)
            # Calcular la distancia Manhattan mínima entre la caja y cualquier objetivo
            min_distance = float('inf')
            for goal in manhattan.map.goals:
                distance = math.fabs(box_instance.x - goal.x) + math.fabs(box_instance.y - goal.y) + player_distance
                min_distance = min(min_distance, distance)

            # Sumar la distancia mínima al total
            total_manhattan_distance += min_distance

        node.add_cost(total_manhattan_distance)
