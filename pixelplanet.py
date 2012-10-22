#!/usr/bin/python
import pygame, sys, os
from pygame.locals import *
from drawing.camera import Camera
from data.world import World
from renderer.renderer import Renderer
from material.materials import Materials

pygame.init()
camera = Camera(1280, 720, pygame.display.set_mode((1280, 720)))
pygame.display.set_caption('Pixel Planet')
world = World(1290,730)
world.generate()

renderer = Renderer(camera);

#print world.to_string()

def input(events):
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
		if event.type == KEYDOWN and event.key == 27:
			sys.exit(0)
		else:
			print(event)

while True:
    input(pygame.event.get())
    renderer.draw(world)
