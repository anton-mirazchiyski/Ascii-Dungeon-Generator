import random

from random_dungeon_layout.config import start_idx, end_idx


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


def handle_corridor_edge_cases_with_dungeon_entrance(row, col):
    if row == start_idx:    # top edge
        row = row + 1
    elif row == end_idx:    # bottom edge
        row = row - 1

    if col == start_idx:   # left edge
        return row, col + 1

    if col == end_idx:     # right edge
        return row, col - 1

    return row, col


def take_user_choice_for_output_save():
    choice = input('Do you want to save output to html file? y/n: ')

    if choice not in ('y', 'n'):
        take_user_choice_for_output_save()

    if choice == 'n':
        return False

    return True
