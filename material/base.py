# -*- coding: utf-8 -*-
import pygame
from data.actions import Action

class Base:
	"""A base material, this material does nothing"""
	id = -1
	mass = 1
	transparency = 0.0
	color = (255,255,255)
	foreground = 1
	
	
	def update(world, position):
		"""Gives the material a chance to update itself.
		Should return a tuple with the action to perform and its argument"""
		return (Action.Idle, 0)
