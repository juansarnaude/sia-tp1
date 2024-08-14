from time import sleep

from models.Sokoban import display_map, find_next_valid_states


def dfs(sokoban_map, sokoban_state):
    frontier_states = [sokoban_state]
    explored_states = set()

    while len(frontier_states) > 0 :
        current_state = frontier_states.pop()

        if current_state.check_win(sokoban_map):
            display_map(sokoban_map, current_state)
            print(current_state.get_steps())
            print("Ganastes")
            return

        # We do this to not revisit the state when we use states
        explored_states.add(current_state)

        # Dont load into the frontier already visited ones
        for next_valid_states in find_next_valid_states(sokoban_map, current_state):
            if next_valid_states not in explored_states:
                frontier_states.append(next_valid_states)
