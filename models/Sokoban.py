import copy

from models.Coordinates import Coordinates
from models.Direction import Direction, get_direction_value

#-----------------------------------------------------------------
#IMMUTABLES THINGS LIKE THE MAP, ARE NOT A PART OF THE STATE BUT LIMIT IT
#-----------------------------------------------------------------

class SokobanMap:
    def __init__(self):
        self.walls = set()
        self.flags = set()

    def add_wall(self, x, y):
        self.walls.add(Coordinates(x,y))

    def add_flag(self, x, y):
        self.flags.add(Coordinates(x,y))



#-----------------------------------------------------------------
#MUTABLE PROPERTIES OF THE SOKOBAN GAME
#-----------------------------------------------------------------

class SokobanState:
    def __init__(self, steps, boxes, player):
        self.steps = steps
        self.boxes = boxes
        self.player = player

    def get_state(self):
        return self.steps, self.boxes, self.player

    def __eq__(self, other):
        if not isinstance(other, SokobanState):
            return False
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.player, frozenset(self.boxes)))

    def check_win(self, soko_map):
        if self.boxes != soko_map.flags:
            return False
        else:
            return True

    #RETURN COPY OF ELEMENTS
    def get_steps(self):
        return self.steps[:]
    def get_boxes(self):
        return self.boxes.copy()
    def get_player(self):
        return copy.deepcopy(self.player)



#-----------------------------------------------------------------

#USEFUL FUNCTIONS FOR MANAGEMENT OF THE STATE THAT REQUIERE THE MAP

#-----------------------------------------------------------------


# RETURN VALID STATES THAT COULD COME FROM THE CURRENT ONE
def find_next_valid_states(soko_map, soko_state):
    next_valid_states_list = []
    directions = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]

    for step_directions in directions:
        current_state_copy = SokobanState(soko_state.get_steps(), soko_state.get_boxes(), soko_state.get_player())
        if move_if_can(soko_map, current_state_copy, step_directions):
            next_valid_states_list.append(current_state_copy)

    return next_valid_states_list

# MOVING AND UPDATING THE STATE IF POSSIBLE
def move_if_can(soko_map, soko_state, direction):
    (step_x, step_y) = get_direction_value(direction)
    new_x = soko_state.player.x + step_x
    new_y = soko_state.player.y + step_y

    if Coordinates(new_x, new_y) in soko_map.walls:
        return False

    if Coordinates(new_x, new_y) in soko_state.boxes:
        box_new_x = new_x + step_x
        box_new_y = new_y + step_y

        if Coordinates(box_new_x, box_new_y) in soko_map.walls or Coordinates(box_new_x, box_new_y) in soko_state.boxes:
            return False

        #Changes position of box and its instance
        soko_state.boxes.discard(Coordinates(new_x,new_y))
        soko_state.boxes.add(Coordinates(box_new_x,box_new_y))

    soko_state.player.move(step_x, step_y)
    soko_state.steps += direction.value
    return True

#FOR PRINTING THE VIEW OF THE MAP
def display_map(soko_map, soko_state):
    width = max(coord.x for coord in soko_map.walls)+1
    height = max(coord.y for coord in soko_map.walls)+1

    print("Now printing map")

    map_grid = [[' ' for _ in range(width)] for _ in range(height)]

    for walls_coord in soko_map.walls:
        map_grid[walls_coord.y][walls_coord.x] = '#'
    for flags_coord in soko_map.flags:
        map_grid[flags_coord.y][flags_coord.x] = '.'
    for box_coord in soko_state.boxes:
        map_grid[box_coord.y][box_coord.x] = '$'
    map_grid[soko_state.player.y][soko_state.player.x] = '@'

    for row in map_grid:
        print(''.join(row))