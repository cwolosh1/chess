class Queen:
	def __init__(self, ID, img):

		self.type = "Queen"
		self.ID = ID
		self.x = chr(100)
		self.captured = False
		self.moved_once = False

		# Denotes white queen
		if self.ID < 1:
			self.y = 1
			self.img = img[0]

		# Denotes black queen
		else:
			self.y = 8
			self.img = img[1]

		self.coords = self.x + str(self.y)

	def up(self, n):
		self.y += n

	def down(self, n):
		self.y -= n

	def left(self, n):
		self.x = chr(ord(self.x) - n)

	def right(self, n):
		self.x = chr(ord(self.x) + n)

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