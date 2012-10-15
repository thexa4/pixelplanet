#!/usr/bin/python
import pygame, sys, os
from pygame.locals import *
from drawing.camera import Camera
from material.base import Base

camera = Camera(1280,720)
base = Base()

pygame.init()
window = pygame.display.set_mode((camera.width, camera.height))
pygame.display.set_caption('Pixel Planet')

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
