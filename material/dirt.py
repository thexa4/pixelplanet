# -*- coding: utf-8 -*-
import pygame
from data.actions import Action

class Dirt:
	"""Dirt"""
	id = 3
	mass = 1
	transparency = 0.0
	color = (128,96,24)
	foreground = 0
	
	
	def update(world, position):
		"""Gives the material a chance to update itself.
		Should return a tuple with the action to perform and its argument"""
		return (Action.Idle, 0)
