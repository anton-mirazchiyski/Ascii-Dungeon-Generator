import random

from random_dungeon_layout.utils import generate_random_room_position, pick_random_room_cell
from random_dungeon_layout.visualizer import mark_room_cell


def position_is_available(row, col, dungeon):
    # a list of unavailable coordinates that keep the rooms spaced out
    unavailable_coordinates = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row - 1, col + 2),
        (row, col), (row, col - 1), (row, col + 1), (row, col + 2),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1), (row + 1, col + 2),
        (row + 2, col - 1), (row + 2, col), (row + 2, col + 1), (row + 2, col + 2),
    ]

    for current_row, current_col in unavailable_coordinates:
        if dungeon[current_row][current_col] != '#':
            return

    return True


def create_room(row, col, dungeon):
    mark_room_cell(dungeon, row, col + 1)
    mark_room_cell(dungeon, row + 1, col + 1)
    mark_room_cell(dungeon, row + 1, col)
    mark_room_cell(dungeon, row, col)


def generate_rooms(dungeon):
    possible_number_of_rooms = random.randint(2, 7)
    random_room_cells = []

    for _ in range(possible_number_of_rooms):
        random_room_position = generate_random_room_position()
        current_row, current_col = random_room_position
        if position_is_available(current_row, current_col, dungeon):
            create_room(current_row, current_col, dungeon)
            random_cell = pick_random_room_cell(current_row, current_col)
            random_room_cells.append(random_cell)

    return random_room_cells
