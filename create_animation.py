import os
import shutil

from PIL import Image
import json
import sys

sprite_map = {
    '#': "./sprites/wall.png",
    '@': "./sprites/monkey.png",
    '$': "./sprites/banana.png",
    '.': "./sprites/target.png",
    '*': "./sprites/banana.png"
}

sprite_size = 360
sprites = {}


for key, path in sprite_map.items():
    sprite = Image.open(path)
    sprites[key] = sprite


def clean_directories():
    try:
        shutil.rmtree("./output/imgs")
    except FileNotFoundError:
        print("Directory './output/imgs' does not exist.")
    except Exception as e:
        print(f"Failed to remove directory './output/imgs'. Reason: {e}")

    try:
        os.makedirs("./output/imgs", exist_ok=True)
        print("Directory './output/imgs' created successfully.")
    except Exception as e:
        print(f"Failed to create directory './output/imgs'. Reason: {e}")

def sokoban_map_update(soko_map, player, direction):
    step = (0,0)
    if direction == "U":
        step = (-1,0)
    if direction == "D":
        step = (1,0)
    if direction == "R":
        step = (0,1)
    if direction == "L":
        step = (0,-1)

    soko_map[player[0]][player[1]] = ' '

    player = (player[0] + step[0], player[1] + step[1])

    if soko_map[player[0]][player[1]] == '$':
        soko_map[player[0]+step[0]][player[1]+step[1]] = '$'

    soko_map[player[0]][player[1]] = '@'

    return soko_map, player



with open(f"{sys.argv[1]}", "r") as file:
    result_file = json.load(file)
    sokoban_map_ini = result_file['initial_map']
    solution_str = result_file['solution']

    #Filter solution
    parts = solution_str.split()
    solution = ''.join(part for part in parts if part != "None")

    #Get the initial map
    sokoban_map = sokoban_map_ini.split('\n')
    sokoban_map = [list(row) for row in sokoban_map]
    player_pos = 0,0

    #Clean output images directories
    clean_directories()

    #Find the player position
    for y, row in enumerate(sokoban_map):
        for x, char in enumerate(row):
            if char == '@':
                player_pos = x,y

    #Set the image sizes
    grid_width = max(len(row) for row in sokoban_map)
    grid_height = len(sokoban_map)
    image_width = grid_width * sprite_size
    image_height = grid_height * sprite_size

    image_counter = 0
    images_file = []
    image_str = ''

    for movement in solution:
        image_counter += 1

        soko_image = Image.new('RGBA', (image_width, image_height))

        for y, row in enumerate(sokoban_map):
            for x, char in enumerate(row):
                if char in sprites:
                    sprite = sprites[char]
                    soko_image.paste(sprite, (x * sprite_size, y * sprite_size, (x+1)* sprite_size, (y+1) * sprite_size))

        image_str = './output/imgs/soko' + str(image_counter) + '.png'
        soko_image.save(image_str)
        images_file.append(image_str)

        sokoban_map, player_pos = sokoban_map_update(sokoban_map, player_pos, movement)


    #Make the GIF
    images = [Image.open(image) for image in images_file]
    images[0].save(
        "./output/solution_animation.gif",
        format="GIF",
        append_images=images[1:],
        save_all=True,
        duration=7,
        loop=0,
        disposal= 2
    )
