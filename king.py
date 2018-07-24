class King:
	def __init__(self, ID, img):

		self.type = "King"
		self.ID = ID
		self.x = chr(101)
		self.captured = False
		self.moved_once = False

		# Denotes white king
		if self.ID < 1:
			self.y = 1
			self.img = img[0]

		# Denotes black king
		else:
			self.y = 8
			self.img = img[1]

		self.coords = self.x + str(self.y)

	def up(self):
		self.y += 1

	def down(self):
		self.y -= 1

	def left(self):
		self.x = chr(ord(self.x) - 1)

	def right(self):
		self.x = chr(ord(self.x) + 1)
		
	def upLeft(self):
		self.y += 1
		self.x = chr(ord(self.x) - 1)

	def upRight(self):
		self.y += 1
		self.x = chr(ord(self.x) + 1)

	def downleft(self):
		self.y -= 1
		self.x = chr(ord(self.x) - 1)

	def downRight(self):
		self.y -= 1
		self.x = chr(ord(self.x) + 1)

	def __str__(self):

		return ("Piece Type: " + self.type + "\n"\
				"ID: " + str(self.ID) + "\n"\
				"Position: " + self.coords + "\n"\
				"Captured: " + str(self.captured) + "\n"\
				"Has Moved: " + str(self.moved_once) + "\n")