# -*- coding: utf-8 -*-
import pygame
from data.actions import Action
from material.materials import Materials

class Dirt:
	"""Dirt"""
	id = 3
	mass = 1
	transparency = 0.0
	color = (255,127,0)
	foreground = 0
	
	
	def update(world, position):
		"""Gives the material a chance to update itself.
		Should return a tuple with the action to perform and its argument"""
		return (Action.Idle, 0)

Materials.add_material(Dirt.id,Dirt);