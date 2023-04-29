import pygame
from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map

def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / 30)
    tile_num_y = int(surface.get_size()[1] / 30)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * 30
            y = row * 30
            new_surf = pygame.Surface((30, 30), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, 30, 30))
            cut_tiles.append(new_surf)

    return cut_tiles

