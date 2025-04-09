import random

import colorama
from colorama import Fore, Style

size = 15
start_idx, end_index = 0, (size - 1)

colorama.init()


def build_dungeon_without_rooms():
    walls = '#' * size
    roomless_dungeon = [list(walls) for _ in range(size)]

    return roomless_dungeon


def determine_start_position(dungeon):
    possible_start_sides = ('top', 'left', 'bottom', 'right')

    random_start_side = random.choice(possible_start_sides)
    random_coordinates = None

    match random_start_side:
        case 'top':
            random_coordinates = (start_idx, random.randint(start_idx, end_index))
        case 'bottom':
            random_coordinates = (end_index, random.randint(start_idx, end_index))
        case 'left':
            random_coordinates = (random.randint(start_idx, end_index), start_idx)
        case 'right':
            random_coordinates = (random.randint(start_idx, end_index), end_index)

    start_row, start_col = random_coordinates
    dungeon[start_row][start_col] = 's'

    return start_row, start_col


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


def mark_room_cell(dungeon, row, col):
    dungeon[row][col] = 'r'


def generate_random_room_position():
    # excludes the edges and keeps the rooms within boundaries
    return random.randint(start_idx + 1, end_index - 2), random.randint(start_idx + 1, end_index - 2)


def create_room(row, col, dungeon):
    mark_room_cell(dungeon, row, col + 1)
    mark_room_cell(dungeon, row + 1, col + 1)
    mark_room_cell(dungeon, row + 1, col)
    mark_room_cell(dungeon, row, col)


def pick_random_room_cell(row, col):
    random_cell_coordinates = random.choice([(row, col + 1), (row + 1, col + 1), (row + 1, col), (row, col)])
    return random_cell_coordinates


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


def mark_corridor_cell(dungeon, row, col):
    dungeon[row][col] = '.'


def is_part_of_corridor(dungeon, row, col):
    return dungeon[row][col] == '.' or dungeon[row][col] in ('↖', '↗', '↙', '↘')


def is_out_of_bounds(row, col):
    return row >= end_index or row <= start_idx or col >= end_index or col <= start_idx


def sort_coordinates_increasingly(coordinates):
    sorted_coordinates = sorted(coordinates, key=lambda x: (x[0], -x[1]))
    return sorted_coordinates


def get_random_room_or_corridor_cell_in_dungeon(dungeon):
    row_idx, column_idx = None, None

    while True:
        row_idx = random.randint(start_idx + 1, end_index - 1)
        row = dungeon[row_idx]
        column_indices = [idx for idx in range(1, len(row) - 1) if row[idx] == '.' or row[idx] == 'r']
        if column_indices:
            column_idx = random.choice(column_indices)
            break

    return row_idx, column_idx


def create_corridor(dungeon, row, col, previous_row, previous_col):
    if row == previous_row and col == previous_col:
        return

    if previous_row == end_index - 1:
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
        elif previous_col == end_index:
            previous_row += 1
            previous_col -= 1
        elif previous_row == start_idx:
            previous_row += 1

        # the recursive function that creates the corridors/paths
        create_corridor(dungeon, current_row, current_col, previous_row, previous_col)


def mark_diagonal_corridor_cell(dungeon, row, col, direction):
    # use unicode arrows for diagonal corridors
    match direction:
        case 'upper-left':
            dungeon[row][col] = '↖'
        case 'upper-right':
            dungeon[row][col] = '↗'
        case 'bottom-left':
            dungeon[row][col] = '↙'
        case 'bottom-right':
            dungeon[row][col] = '↘'


def mark_dead_end_corridor(dungeon, row, col):
    dungeon[row][col] = '|'


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


def print_dungeon(dungeon):
    print()
    for row in dungeon:
        colored_row = []

        for element in row:
            if element == 'r':
                colored_row.append(Fore.BLUE + element + Style.RESET_ALL)
            elif element in ('.', 's', '↖', '↗', '↙', '↘'):
                colored_row.append(Fore.YELLOW + element + Style.RESET_ALL)
            elif element == '|':
                colored_row.append(Fore.RED + element + Style.RESET_ALL)
            else:
                colored_row.append(element)

        print(*colored_row, sep=' ')


def generate_dungeon():
    dungeon = build_dungeon_without_rooms()
    row_start, col_start = determine_start_position(dungeon)
    rooms_coordinates = generate_rooms(dungeon)
    sorted_rooms_coordinates = sort_coordinates_increasingly(rooms_coordinates + [(row_start, col_start)])
    generate_corridors_between_rooms(dungeon, sorted_rooms_coordinates)
    generate_additional_corridors(dungeon)
    print_dungeon(dungeon)


if __name__ == '__main__':
    generate_dungeon()
