from models.Coordinates import Coordinates
from models.Direction import Direction
from models.Map import Map


def box_stuck(node = None, map = None):
    if map:
        box_stuck.map = MapWithMarkedStuckPoints(map)
        return
    else:
        if box_stuck.map.check_stuck_boxes(node.state.boxes):
            node.add_cost(999999)
        return


# MapWithMarkedStuckPoints is an extension of the map class, the only difference
# they have is just that this class has marked the stuck points in which if a box lands there
# the level is unsolvable
class MapWithMarkedStuckPoints(Map):
    def __init__(self, map):
        self.grid = map.grid
        self.goals = map.goals
        self.stuck_points = set()

        self.limit_corners()

        self.expand_limited()

        # Visualization of stuck points
        for coord in self.stuck_points:
            x, y = coord.x, coord.y
            self.grid[y][x] = '%'

        map_string = ''
        for row in self.grid:
            map_string += ''.join(row)
            map_string += '\n'

        print(map_string)

    # Just limit the corners because boxes get stuck there
    def limit_corners(self):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                current_coord = Coordinates(x, y)
                if not self.is_wall(current_coord):
                    if self.is_corner(x, y) and not self.is_goal(current_coord):
                        if self.is_inside(current_coord):
                            self.stuck_points.add(current_coord)

    #Function to check if a stuck point is inside the limits of the map
    # We just check if it crashes first beetween the out of size or out or index
    def is_inside(self, coord):
        for direction in Direction:
            coord_copy = Coordinates(coord.x, coord.y)
            while 1:
                try:
                    if self.is_wall(coord_copy):
                        break
                except IndexError:
                    return False
                coord_copy = coord_copy.move(direction)

                if coord_copy.x < 0 or coord_copy.y < 0:
                    return False
        return True

    # We check lines between all points that are in line horizontally or vertically
    # and check if that line has a wall on the side constantly AND does not have a flag inside
    # next to that walls
    def expand_limited(self):
        # To not explore the same node-node relation
        explored_stuck_points = set()

        for stuck_point_1 in self.stuck_points.copy():
            for stuck_point_2 in self.stuck_points.copy():

                if stuck_point_2 not in explored_stuck_points:
                    if stuck_point_1.x == stuck_point_2.x:

                        if stuck_point_1.y > stuck_point_2.y:
                            try:
                                if self.is_wall(Coordinates(stuck_point_1.x-1, stuck_point_1.y)):
                                    self.check_line_between_points(stuck_point_1.x-1, stuck_point_1.y, stuck_point_1, stuck_point_2, Direction.UP)
                            except IndexError:
                                pass

                        elif stuck_point_1.y < stuck_point_2.y:
                            try:
                                if self.is_wall(Coordinates(stuck_point_1.x+1, stuck_point_1.y)):
                                    self.check_line_between_points(stuck_point_1.x+1, stuck_point_1.y, stuck_point_1, stuck_point_2, Direction.DOWN)
                            except IndexError:
                                pass

                    elif stuck_point_1.y == stuck_point_2.y:

                        if stuck_point_1.x > stuck_point_2.x:
                            try:
                                if self.is_wall(Coordinates(stuck_point_1.x, stuck_point_1.y-1)):
                                    self.check_line_between_points(stuck_point_1.x, stuck_point_1.y-1, stuck_point_1, stuck_point_2, Direction.LEFT)
                            except IndexError:
                                pass

                        elif stuck_point_1.x < stuck_point_2.x:
                            try:
                                if self.is_wall(Coordinates(stuck_point_1.x, stuck_point_1.y+1)):
                                    self.check_line_between_points(stuck_point_1.x, stuck_point_1.y+1, stuck_point_1, stuck_point_2, Direction.RIGHT)
                            except IndexError:
                                pass



    # Check if the line between points has a wall by the side constantly
    # and also check if theres no a flag between both.
    def check_line_between_points(self, x, y, stuck_point_1, stuck_point_2, iterator_direction):
        wall_coord = Coordinates(x,y)
        line_coord = Coordinates(stuck_point_1.x, stuck_point_1.y)
        aux_to_add = set()
        while line_coord != stuck_point_2:
            if self.is_goal(line_coord) or not self.is_wall(wall_coord):
                return
            else:
                aux_to_add.add(line_coord)
                wall_coord = wall_coord.move(iterator_direction)
                line_coord = line_coord.move(iterator_direction)
        for aux in aux_to_add:
            self.stuck_points.add(aux)

    def is_corner(self, x, y):
        try:
            left_side = self.is_wall(Coordinates(x-1,y))
            right_side = self.is_wall(Coordinates(x+1,y))
            top_side = self.is_wall(Coordinates(x,y-1))
            bottom_side = self.is_wall(Coordinates(x,y+1))
        except IndexError:
            return False

        if left_side and top_side:
            return True
        elif left_side and bottom_side:
            return True
        elif right_side and bottom_side:
            return True
        elif right_side and top_side:
            return True
        else:
            return False

    def check_stuck_boxes(self, boxes):
        for box in boxes:
            if box in self.stuck_points:
                return True
        return False