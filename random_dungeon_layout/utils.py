import random

from random_dungeon_layout.config import start_idx, end_idx
from random_dungeon_layout.visualizer import mark_treasure, mark_dead_end_corridor


def generate_random_room_position():
    # excludes the edges and keeps the rooms within boundaries
    return random.randint(start_idx + 1, end_idx - 2), random.randint(start_idx + 1, end_idx - 2)


def pick_random_room_cell(row, col):
    random_cell_coordinates = random.choice([(row, col + 1), (row + 1, col + 1), (row + 1, col), (row, col)])
    return random_cell_coordinates


def is_part_of_corridor(dungeon, row, col):
    return dungeon[row][col] == '.' or dungeon[row][col] in ('↖', '↗', '↙', '↘')


def is_out_of_bounds(row, col):
    return row >= end_idx or row <= start_idx or col >= end_idx or col <= start_idx


def sort_coordinates_increasingly(coordinates):
    sorted_coordinates = sorted(coordinates, key=lambda x: (x[0], -x[1]))
    return sorted_coordinates


def get_random_room_or_corridor_cell_in_dungeon(dungeon):
    row_idx, column_idx = None, None

    while True:
        row_idx = random.randint(start_idx + 1, end_idx - 1)
        row = dungeon[row_idx]
        column_indices = [idx for idx in range(1, len(row) - 1) if row[idx] == '.' or row[idx] == 'r']
        if column_indices:
            column_idx = random.choice(column_indices)
            break

    return row_idx, column_idx


def determine_dead_end_or_treasure(dungeon, row, col):
    # some chance to spawn a treasure at the end of an unconnected corridor, otherwise - dead-end
    if random.random() <= 0.2:
        mark_treasure(dungeon, row, col)
    else:
        mark_dead_end_corridor(dungeon, row, col)
