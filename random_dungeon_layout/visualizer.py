from random_dungeon_layout.colors import ROOM, CORRIDOR, DEAD_END_CORRIDOR, ENTRANCE, TREASURE, RESET


def mark_entrance(dungeon, row, col):
    dungeon[row][col] = 's'


def mark_room_cell(dungeon, row, col):
    dungeon[row][col] = 'r'


def mark_corridor_cell(dungeon, row, col):
    dungeon[row][col] = '.'


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


def mark_treasure(dungeon, row, col):
    dungeon[row][col] = '!'


def print_dungeon(dungeon):
    print()
    for row in dungeon:
        colored_row = []

        for element in row:
            if element == 'r':
                colored_row.append(ROOM + element + RESET)
            elif element in ('.', '↖', '↗', '↙', '↘'):
                colored_row.append(CORRIDOR + element + RESET)
            elif element == 's':
                colored_row.append(ENTRANCE + element + RESET)
            elif element == '|':
                colored_row.append(DEAD_END_CORRIDOR + element + RESET)
            elif element == '!':
                colored_row.append(TREASURE + element + RESET)
            else:
                colored_row.append(element)

        print(*colored_row, sep=' ')
