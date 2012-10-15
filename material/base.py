import pygame

class Base:
	"""A base material, this material does nothing"""
	id = -1
	mass = 1
	transparency = 0.0
	color = pygame.Color("white")
	
	def update(world, position):
		return 0