class Camera:
	"""A 2d camera"""
	
	def __init__(self, width, height, window):
		self.width = width
		self.height = height
		self.x = 0
		self.y = 0
		self.window = window