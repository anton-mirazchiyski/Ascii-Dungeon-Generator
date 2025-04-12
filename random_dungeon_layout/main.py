from random_dungeon_layout.dungeon import generate_dungeon
from random_dungeon_layout.visualizer import print_dungeon, save_output_to_html_file


if __name__ == '__main__':
    dungeon = generate_dungeon()
    print_dungeon(dungeon)
    # save_output_to_html_file(dungeon)
