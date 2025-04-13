# **Procedural Dungeon Generator**

_A Python program 🐍 for generating random dungeon layouts with entrance, rooms and corridors._


## Features

- ✔️ Randomly generated dungeon layouts
- ✔️ Rooms connected by corridors
- ✔️ Basic ASCII visualization in the console
- ✔️ Procedural generation principles
- ✔️ Choice to save interesting generations/outputs to an HTML file


## Example Outputs

![Dungeon-2](https://github.com/user-attachments/assets/2999ce52-8e64-476c-8efb-90e448af4212)


![Dungeon-3](https://github.com/user-attachments/assets/ff49b12d-bd5e-4517-8685-611c99ed18d0)


![Dungeon-4](https://github.com/user-attachments/assets/0c9e5293-298b-42c7-987c-55fd3688eeb0)


Added more corridors (including diagonal ones) to make the dungeon more interesting, diverse and have more exploration options.
There could be dead-end corridors.

![Dungeon-12](https://github.com/user-attachments/assets/517b2e05-1965-42e6-8afe-bd1159e1d883)


![Dungeon-16](https://github.com/user-attachments/assets/835eb208-a41e-4b9d-88bc-0d7780488473)



![Dungeon-13](https://github.com/user-attachments/assets/006792b8-dad8-4d5a-94af-4455215616dd)


![Dungeon-14](https://github.com/user-attachments/assets/4b4f4f2e-bc82-417e-9a9e-4f14eb826372)


![Dungeon-22](https://github.com/user-attachments/assets/0a1d830c-5c57-4a49-8a8a-395e790ac504)



### Representations:

- Rooms (squares of 'r' letters) - 🟦
- Corridors - 🟨
-   - linear - dots
-   - diagonal - arrows
- Entrance ('s') - 🟨
- Walls (#) - ⬜
- Dead-end corridors ('|') - 🟥
- Treasures (!) - 🟩

## Example Outputs saved in HTML file

![Screenshot 2025-04-13 at 23-06-30 Generated Dungeon](https://github.com/user-attachments/assets/07f0146d-a68e-4808-a0e5-8ff48c2d0d21)


![Screenshot 2025-04-13 at 23-09-31 Generated Dungeon](https://github.com/user-attachments/assets/6dc3345c-a0cf-42d8-b1f0-fe9c04d60c3a)



## Installation and Usage

1. Clone the repository:

```
git clone https://github.com/anton-mirazchiyski/Ascii-Dungeon-Generator.git
```

2. Install dependencies inside a virtual environment:

```
pip install -r requirements.txt
```

3. Run the script to generate a random dungeon layout:

```
python -m random_dungeon_layout.main
```
or navigate to the ```main.py``` module and run it manually

## Tip: Disable Input Prompting

If you don't want to be prompted for input after each generation, you can just comment out the
```save_output_to_html_file()``` function in the ```if __name__ == '__main__'``` block


## Feedback & Suggestions

If you have any feedback, feel free to message me! I'm always open to suggestions.

Feel free to add a ⭐ if you liked this.

Discussions are open.
