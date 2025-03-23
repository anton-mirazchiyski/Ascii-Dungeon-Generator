import random

size = 10
start_idx, end_index = 0, (size - 1)


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
    dungeon[start_row][start_col] = '.'


def position_is_available(row, col, dungeon):
    if row + 1 > end_index - 1 or col + 1 > end_index - 1:
        return False

    conditions = [
        dungeon[row][col] == '#' ,
        dungeon[row - 1][col] == '#',
        dungeon[row + 1][col] == '#',
        dungeon[row][col - 1] == '#',
        dungeon[row][col + 1] == '#',
        dungeon[row + 2][col] == '#',
        dungeon[row][col + 2] == '#'
    ]
    return all(conditions)


def mark_cell(dungeon, row, col):
    dungeon[row][col] = '.'


def generate_random_room_position():
    return random.randint(start_idx + 1, end_index - 1), random.randint(start_idx + 1, end_index - 2) # excludes the edges


def create_room(row, col, dungeon):
    mark_cell(dungeon, row, col + 1)
    mark_cell(dungeon, row + 1, col + 1)
    mark_cell(dungeon, row + 1, col)
    mark_cell(dungeon, row, col)


def generate_rooms(dungeon):
    number_of_rooms = random.randint(2, 6)

    for _ in range(number_of_rooms):
        random_room_position = generate_random_room_position()
        current_row, current_col = random_room_position
        if position_is_available(current_row, current_col, dungeon):
            create_room(current_row, current_col, dungeon)


dungeon = build_dungeon_without_rooms()
determine_start_position(dungeon)
generate_rooms(dungeon)

for row in dungeon:
    print(*row, sep='')
