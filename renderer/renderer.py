import pygame


class Renderer:
	"""Renders an image of the PixelPlanet"""
	def __init__(self, camera):
		self.camera = camera

	def draw(self, world):
		"We slice a part of the worldarray that fits within our camera"
		worldarray = world.get_colors()
		pxarray = pygame.PixelArray(self.camera.window)

		for y in range(len(pxarray) - 1):
			for x in range(len(pxarray[y]) - 1):
				pxarray[y][x] = worldarray[x][y]

		newwindow = pxarray.make_surface()
		self.camera.window = self.camera.window.copy()
		self.camera.window.blit(newwindow, newwindow.get_rect())
		pygame.display.flip()
