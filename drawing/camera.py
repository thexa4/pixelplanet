class Camera:
	"""A 2d camera"""
	x = 0
	y = 0
	width = 0
	height = 0
	
	def __init__(self, width, height):
		self.width = width
		self.height = height