import pygame
from support import import_csv_layout
from support import import_cut_graphics
from tiles import Tile, StaticTile

class Level:
	def __init__(self, level_data, surface):
		# general setup
		self.display_surface = surface
		terrain_layout = import_csv_layout(level_data['terrain'])
		self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
	def create_tile_group(self,layout,type):
		sprite_group = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * 30
					y = row_index * 30
					if type == 'terrain':
						terrain_tile_list = import_cut_graphics('graphics/terrain_atlas.png')
						tile_surface = terrain_tile_list[int(val)-1]
						sprite = StaticTile(30,x,y, tile_surface)

	def run(self):
		self.terrain_sprites.draw(self.display_surface)
