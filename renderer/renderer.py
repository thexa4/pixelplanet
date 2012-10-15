import pygame


class Renderer:
	"""Renders an image of the PixelPlanet"""
	def __init__(self, camera):
		self.camera = camera
	
	def draw(self, world):
			