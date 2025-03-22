size = 10

def build_dungeon_without_rooms():
    walls = '#' * size
    roomless_dungeon = [walls for _ in range(size)]

    return roomless_dungeon


dungeon = build_dungeon_without_rooms()

for row in dungeon:
    print(*row, sep='')
