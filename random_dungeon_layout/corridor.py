import random

from random_dungeon_layout.config import end_idx, start_idx
from random_dungeon_layout.utils import is_out_of_bounds, get_random_room_or_corridor_cell_in_dungeon
from random_dungeon_layout.visualizer import mark_corridor_cell, mark_dead_end_corridor, mark_diagonal_corridor_cell


def create_corridor(dungeon, row, col, previous_row, previous_col):
    if row == previous_row and col == previous_col:
        return

    if previous_row == end_idx - 1:
        if col > previous_col:
            create_corridor(dungeon, row, col, previous_row, previous_col + 1)  # move towards the right

        if col < previous_col:
            create_corridor(dungeon, row, col, previous_row, previous_col - 1)  # move towards the left

    if is_out_of_bounds(previous_row, previous_col):
        return

    if dungeon[previous_row][previous_col] == '#':
        mark_corridor_cell(dungeon, previous_row, previous_col)

    # chooses a direction for the path
    if row != previous_row:
        return create_corridor(dungeon, row, col, previous_row + 1, previous_col) # move downwards

    if col > previous_col:
        return create_corridor(dungeon, row, col, previous_row, previous_col + 1)  # move towards the right

    elif col < previous_col:
        return create_corridor(dungeon, row, col, previous_row, previous_col - 1)  # move towards the left


def generate_corridors_between_rooms(dungeon, rooms_coordinates):
    for idx in range(1, len(rooms_coordinates)):
        current_row, current_col = rooms_coordinates[idx]
        previous_row, previous_col = rooms_coordinates[idx - 1]

        # handles edge cases with the dungeon entrance
        if previous_col == start_idx:
            previous_row += 1
            previous_col += 1
        elif previous_col == end_idx:
            previous_row += 1
            previous_col -= 1
        elif previous_row == start_idx:
            previous_row += 1

        # the recursive function that creates the corridors/paths
        create_corridor(dungeon, current_row, current_col, previous_row, previous_col)


def handle_diagonal_corridor_end(dungeon, direction, corridor, diagonal_directions):
    opposite_diagonal_directions = {
        'upper-left': lambda r, c: (r + 1, c + 1),
        'upper-right': lambda r, c: (r + 1, c - 1),
        'bottom-left': lambda r, c: (r - 1, c + 1),
        'bottom-right': lambda r, c: (r - 1, c - 1)
    }

    last_corridor_part = corridor[-1]
    last_row, last_column = last_corridor_part

    current_row, current_column = diagonal_directions[direction](last_row, last_column)

    if is_out_of_bounds(current_row, current_column):
        current_row, current_column = opposite_diagonal_directions[direction](current_row, current_column)
        mark_dead_end_corridor(dungeon, current_row, current_column)

    if dungeon[current_row][current_column] == '#':
        mark_dead_end_corridor(dungeon, current_row, current_column)


def generate_additional_corridors(dungeon):
    linear_directions_mapping = {
        # linear directions
        'upwards': lambda r, c: (r - 1, c),
        'downwards': lambda r, c: (r + 1, c),
        'left': lambda r, c: (r, c - 1),
        'right': lambda r, c: (r, c + 1),
    }

    diagonal_directions_mapping = {
        # diagonal directions
        'upper-left': lambda r, c: (r - 1, c - 1),
        'upper-right': lambda r, c: (r - 1, c + 1),
        'bottom-left': lambda r, c: (r + 1, c - 1),
        'bottom-right': lambda  r, c: (r + 1, c + 1)
    }

    all_directions = {**linear_directions_mapping, **diagonal_directions_mapping}
    possible_directions = [direction for direction in all_directions.keys()]
    linear_directions, diagonal_directions = possible_directions[:4], possible_directions[4:]

    diagonal_corridors_limit = 2
    diagonal_corridors_count = 0

    for i in range(random.randint(3, 7)):
        row, column = get_random_room_or_corridor_cell_in_dungeon(dungeon)
        direction = random.choice(possible_directions)

        corridor = []

        for j in range(random.randint(3, 7)):
            row, column = all_directions[direction](row, column)

            if is_out_of_bounds(row, column):
                break

            # prevents diagonal corridors crossing over structures
            if dungeon[row][column] != '#' and direction in diagonal_directions:
                break
            if diagonal_corridors_count >= diagonal_corridors_limit and direction in diagonal_directions:
                direction = random.choice(linear_directions)
                continue

            if dungeon[row][column] == '#':
                if direction in linear_directions:
                    mark_corridor_cell(dungeon, row, column)
                else:
                    mark_diagonal_corridor_cell(dungeon, row, column, direction)
                corridor.append((row, column))

        # removes a one-cell corridor
        if len(corridor) == 1:
            previous_row, previous_col = corridor[0]
            dungeon[previous_row][previous_col] = '#'
            corridor.clear()

        if corridor and direction in diagonal_directions:
            diagonal_corridors_count += 1
            handle_diagonal_corridor_end(dungeon, direction, corridor, diagonal_directions_mapping)
