

def boxes_in_goals(node = None, map = None):
    if not hasattr(boxes_in_goals, "map"):
        boxes_in_goals.map = map
        boxes_in_goals.n_boxes = len(map.boxes)
        return
    else:
        node.add_cost(- len(node.state.boxes.intersection(boxes_in_goals.map.goals)) / boxes_in_goals.n_boxes)
        return

