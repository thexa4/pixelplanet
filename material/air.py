# -*- coding: utf-8 -*-
import pygame
from data.actions import Action
from material.materials import Materials

class Air:
	"""Air"""
	id = 4
	mass = 1
	transparency = 0.0
	color = (0,0,255)
	foreground = 1
	
	
	def update(world, position):
		"""Gives the material a chance to update itself.
		Should return a tuple with the action to perform and its argument"""
		return (Action.Idle, 0)

Materials.add_material(Air.id,Air);