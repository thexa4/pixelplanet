class World:
	
	def __init__(self, width, height):
		self.width   = width
		self.height  = height
		self.grid    = []
		for y in range(width):
			row = []
			for x in range(height):
				row.append([])
			self.grid.append(row)
		
		self.light   = [[0.0] * width] * height
		self.gravity = [[(0.0, 0.0)] * width] * height
	
	def generate(self):
		
		cx = self.width / 2
		cy = self.height / 2
		r  = 0.75 * min(cx, cy)
		
		for x in range(self.width):
			for y in range(self.height):
				if (x - cx)**2 + (y - cy)**2 < r**2:
					self.grid[y][x] = [0]
		
		self.update_gravity()
	
	def update(self):
		self.update_material()
		self.update_light()
	
	def update_material(self):
		pass
	
	def update_light(self):
		pass
	
	def update_gravity(self):
		pass
	
	def to_string(self):
		res = ''
		
		for y in range(self.height):
			for x in range(self.width):
				cell = self.grid[y][x]
				if cell == []:
					res += ' '
				else:
					res += str(cell[0])
			res += '\n'
		
		return res
