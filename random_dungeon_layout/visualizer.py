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


def save_output_to_html_file(dungeon):
    styles = '''
        body {
            background-color: #202225;
            color: #dfd7d7;
            font-family: sans-serif;
            font-size: 1rem;
            display: flex;
            min-width: 100vh;
            flex-direction: column;
            align-items: center;
            gap: 2rem;
        }
        
        h1 {
            margin-top: 2rem;
            font-weight: bold;
        }
        
        p {
            line-height: 0.9;
        }
        
        span {
            display: inline-block;
            margin-right: 0.5rem;
            min-width: 0.8rem;
            padding: 0 0.2rem;
        }
        
        .dungeon {
            text-align: center;
            font-size: 1.25rem;
            padding: 1rem;
        }
        
        .entrance {
            color: #996a19;
        }
        
        .room {
            color: #2362c0;
        }
        
        .corridor {
            color: #996a19;
        }
        
        .dead-end {
            color: #ce3b2d;
        }
        
        .treasure {
            color: #35a113;
        }
    '''

    document_title = 'Generated Dungeon'
    first_heading = 'Random Dungeon Layout'

    output_result = ''

    classes = {'r': 'room', '.': 'corridor', '↖' : 'corridor', '↗' : 'corridor', '↙' : 'corridor', '↘': 'corridor',
                's': 'entrance', '|': 'dead-end',  '!': 'treasure', '#': 'wall',}

    for row in dungeon:
        paragraph = '<p>' + ''.join([f'<span class="{classes[element]}">{element}</span>' for element in row]) + '</p>\n'
        output_result += paragraph

    html_content = f'''
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{document_title}</title>
            <style>
                {styles}
            </style>
         </head>
        <body>
            <h1>{first_heading}</h1>
            <div class="dungeon">
                {output_result}
            </div>
        </body>
        </html>
    '''

    with open('export/dungeon-layout.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
