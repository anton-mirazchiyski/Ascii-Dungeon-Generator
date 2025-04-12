import random

from random_dungeon_layout.config import SIZE, start_idx, end_idx
from random_dungeon_layout.corridor import generate_corridors_between_rooms, generate_additional_corridors
from random_dungeon_layout.room import generate_rooms
from random_dungeon_layout.utils import sort_coordinates_increasingly
from random_dungeon_layout.visualizer import mark_entrance


def build_dungeon_without_rooms():
    walls = '#' * SIZE
    roomless_dungeon = [list(walls) for _ in range(SIZE)]

    return roomless_dungeon


def determine_start_position(dungeon):
    possible_start_sides = ('top', 'left', 'bottom', 'right')

    random_start_side = random.choice(possible_start_sides)
    random_coordinates = None

    match random_start_side:
        case 'top':
            random_coordinates = (start_idx, random.randint(start_idx, end_idx))
        case 'bottom':
            random_coordinates = (end_idx, random.randint(start_idx, end_idx))
        case 'left':
            random_coordinates = (random.randint(start_idx, end_idx), start_idx)
        case 'right':
            random_coordinates = (random.randint(start_idx, end_idx), end_idx)

    start_row, start_col = random_coordinates
    mark_entrance(dungeon, start_row, start_col)

    return start_row, start_col


def generate_dungeon():
    dungeon = build_dungeon_without_rooms()
    row_start, col_start = determine_start_position(dungeon)
    rooms_coordinates = generate_rooms(dungeon)
    sorted_rooms_coordinates = sort_coordinates_increasingly(rooms_coordinates + [(row_start, col_start)])
    generate_corridors_between_rooms(dungeon, sorted_rooms_coordinates)
    generate_additional_corridors(dungeon)

    return dungeon
