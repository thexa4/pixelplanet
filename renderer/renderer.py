import pygame


class Renderer:
	"""Renders an image of the PixelPlanet"""
	def __init__(self, camera):
		self.camera = camera
	
	def draw(self, world):
		worldarray = world.2darray()
		pxarray = pygame.PixelArray(self.camera.window)
		#Slice worldarray to fit in pxarray using camera
		for y in range(len(pxarray)):
			for x in range(len(pxarray[y])):
				pxarray[y][x] = worldarray[y][x]
		
		newwindow = pxarray.make_surface()
		self.camera.window.blit(newwindow, newwindow.get_rect())
		pygame.display.flip()