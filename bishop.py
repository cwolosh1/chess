class Bishop:
	def __init__(self, ID, img):

		self.type = "Bishop"
		self.ID = ID
		self.x = chr(99 + 3*(self.ID % 2))
		self.captured = False
		self.moved_once = False

		# Denotes white bishop
		if self.ID < 2:
			self.y = 1
			self.img = img[0]

		# Denotes black bishop
		else:
			self.y = 8
			self.img = img[1]

		self.coords = self.x + str(self.y)

	def upLeft(self, n):
		self.y += n
		self.x = chr(ord(self.x) - n)

	def upRight(self, n):
		self.y += n
		self.x = chr(ord(self.x) + n)

	def downleft(self, n):
		self.y -= n
		self.x = chr(ord(self.x) - n)

	def downRight(self, n):
		self.y -= n
		self.x = chr(ord(self.x) + n)

	def __str__(self):

		return ("Piece Type: " + self.type + "\n"\
				"ID: " + str(self.ID) + "\n"\
				"Position: " + self.coords + "\n"\
				"Captured: " + str(self.captured) + "\n"\
				"Has Moved: " + str(self.moved_once) + "\n")