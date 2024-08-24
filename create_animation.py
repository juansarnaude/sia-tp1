import pygame
import json
import sys
from pygame.locals import *

TILE_SIZE = 32  # Tamaño reducido de las imágenes

SPRITE_MAP = {
    '#': 'wall.png',
    '$': 'banana.png',  # Caja
    '.': 'target.png',  # Objetivo
    '*': 'banana.png',  # Caja en objetivo
    '+': 'monkey.png',  # Jugador en objetivo
    '@': 'monkey.png'  # Jugador
}


def load_sprites():
    sprites = {}
    for char, filename in SPRITE_MAP.items():
        sprite = pygame.image.load(f'sprites/{filename}')
        sprite = pygame.transform.scale(sprite, (TILE_SIZE, TILE_SIZE))  # Redimensionar a 32x32
        sprites[char] = sprite
    return sprites


def create_background_surface(grid, sprites):
    background_surface = pygame.Surface((len(grid[0]) * TILE_SIZE, len(grid) * TILE_SIZE))
    background_surface.fill((0, 0, 0))  # Color de fondo opcional

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in '.':
                background_surface.blit(sprites['.'], (x * TILE_SIZE, y * TILE_SIZE))
            elif char in '*':
                background_surface.blit(sprites['.'], (x * TILE_SIZE, y * TILE_SIZE))
            elif char in '+':
                background_surface.blit(sprites['.'], (x * TILE_SIZE, y * TILE_SIZE))

    return background_surface


def draw_map(screen, grid, sprites, background_surface):
    # Primero dibujar la superficie de fondo con los targets y las cajas en objetivos
    screen.blit(background_surface, (0, 0))

    # Luego dibujar las paredes y cajas
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                screen.blit(sprites[char], (x * TILE_SIZE, y * TILE_SIZE))
            elif char in '$@+*':
                screen.blit(sprites[char], (x * TILE_SIZE, y * TILE_SIZE))


def move_player(grid, position, direction):
    x, y = position
    new_x, new_y = x, y

    if direction == 'R':
        new_x += 1
    elif direction == 'L':
        new_x -= 1
    elif direction == 'U':
        new_y -= 1
    elif direction == 'D':
        new_y += 1

    target_cell = grid[new_y][new_x]


    if target_cell in ' .':
        grid[y][x] = ' ' if grid[y][x] == '@' else '.'
        grid[new_y][new_x] = '@'
        return [new_x, new_y]

    elif target_cell == '$' or target_cell == '*':
        beyond_x, beyond_y = new_x + (new_x - x), new_y + (new_y - y)

        beyond_cell = grid[beyond_y][beyond_x]

        if beyond_cell in ' .':
            grid[new_y][new_x] = '@' if target_cell == '$' else '+'
            grid[beyond_y][beyond_x] = '*' if beyond_cell == '.' else '$'

            grid[y][x] = ' ' if grid[y][x] == '@' else '.'

            return [new_x, new_y]

    return position



with open(f"{sys.argv[1]}", "r") as f:
    data = json.load(f)

if data['status']=='failure':
    print("No solutions found")
    sys.exit()

initial_map = data['initial_map'].splitlines()
solutions_list=[]
for solution in data['solution']:
    solutions_list.append(solution)

max_width = max(len(row) for row in initial_map)
height = len(initial_map)

# Tamaño de la ventana
width = max_width * TILE_SIZE
height = height * TILE_SIZE

for solution in solutions_list:
    pygame.init()
    print("Solution: " + str(solution))
    screen = pygame.display.set_mode((width, height))

    # Cargar sprites
    sprites = load_sprites()

    # Posición inicial del jugador
    player_pos = None
    for y, row in enumerate(initial_map):
        if '@' in row:
            player_pos = [row.index('@'), y]
            break
        elif '+' in row:
            player_pos = [row.index('+'), y]
            break

    # Cargar mapa en formato de grid
    grid = []
    for line in initial_map:
        grid.append(list(line))

    # Crear superficie de fondo
    background_surface = create_background_surface(grid, sprites)

    # Loop principal
    clock = pygame.time.Clock()
    move_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if move_index < len(solution):
            # Limpiar la pantalla antes de dibujar
            screen.fill((0, 0, 0))

            # Actualizar la posición del jugador según el movimiento actual
            player_pos = move_player(grid, player_pos, solution[move_index])

            draw_map(screen, grid, sprites, background_surface)
            pygame.display.flip()

            # Pasar al siguiente movimiento
            move_index += 1

            clock.tick(5)
        else:
            # Si se han realizado todos los movimientos, mantener la ventana abierta
            draw_map(screen, grid, sprites, background_surface)
            pygame.display.flip()
            clock.tick(5)

    pygame.quit()
