# -*- coding: utf-8 -*-
from material.materials import Materials


class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def copy(self):
		return Vector2(self.x, self.y)
	
	def substract(self, other):
		self.x -= other.x
		self.y -= other.y
	
	def add(self, other):
		self.x += other.x
		self.y += other.y
	
	def scale(self, s):
		self.x *= s
		self.y *= s
	
	def length(self):
		return (self.x**2 + self.y**2)**.5


class World:
	
	def __init__(self, width, height):
		self.width   = width
		self.height  = height
		self.grid    = [[[] for x in xrange(width)] for y in xrange(height)]
		self.light   = [[0.0 for x in xrange(width)] for y in xrange(height)]
		self.gravity = [[Vector2(0.0,0.0) for x in xrange(width)] for y in xrange(height)]
	
	def generate(self):
		
		cx = self.width / 2
		cy = self.height / 2
		r  = 0.75 * min(cx, cy)
		
		for x in xrange(self.width):
			for y in xrange(self.height):
				dist = (x - cx)**2 + (y - cy)**2
				radius = r**2
				self.grid[y][x] = []
				if dist < radius:
					self.grid[y][x] = [3]
				if dist < radius * 0.9:
					self.grid[y][x] = [2]
				if dist < radius * 0.2:
					self.grid[y][x] = [1]
		
		#self.update_gravity()
	
	def update(self):
		self.update_material()
		self.update_light()
	
	def update_material(self):
		pass
	
	def update_light(self):
		pass
	
	def update_gravity(self):
		
		for x in xrange(self.width):
			for y in xrange(self.height):
				
				c = Vector2(x, y)
				g = Vector2(0.0, 0.0)
				
				for ox in xrange(self.width):
					for oy in xrange(self.height):
						
						o = Vector2(ox, oy)
						cell = self.grid[oy][ox]
						
						v = o.copy()
						v.substract(c)
						l = v.length()
						if l == 0:
							continue
						
						m = 0.0
						for pixel in cell:
							# Mass of pixel
							m += Materials.materials[pixel].mass
						
						v.scale(m / l**3)
						g.add(v)
				
				self.gravity[y][x] = g
	
	def to_string(self):
		res = ''
		
		res += 'Material map:\n'
		for y in xrange(self.height):
			for x in xrange(self.width):
				cell = self.grid[y][x]
				if cell == []:
					res += '   '
				else:
					res += ' %2d' % (cell[0])
			res += '\n'
		
		res += '\nGravity vector map:\n'
		for y in xrange(self.height):
			for x in xrange(self.width):
				g = self.gravity[y][x]
				res += ' (%05.2f,%05.2f)' % (g.x, g.y)
			res += '\n'
		
		res += '\nGravity value map:\n'
		for y in xrange(self.height):
			for x in xrange(self.width):
				g = self.gravity[y][x]
				res += ' %04.2f' % (g.length())
			res += '\n'
		
		return res
	
	def get_colors(self):
		print Materials.materials
		
		color = [[(0, 0, 0) for x in xrange(self.width)] for y in xrange(self.height)]
		
		for y in xrange(self.height):
			for x in xrange(self.width):
				cell = self.grid[y][x]
				if cell != []:
					color[y][x] = Materials.materials[cell[0]].color
		
		return color
