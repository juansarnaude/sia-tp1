

def boxes_in_goals(node = None, map = None):
    if not hasattr(boxes_in_goals, "map"):
        boxes_in_goals.map = map
        return
    else:
        node.add_cost(- len(node.state.boxes.intersection(boxes_in_goals.map.goals)))
        return

