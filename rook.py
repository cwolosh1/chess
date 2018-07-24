class Rook:
	def __init__(self, ID, img):

		self.type = "Rook"
		self.ID = ID
		self.x = chr(97 + 7*(self.ID % 2))
		self.captured = False
		self.moved_once = False

		# Denotes white rook
		if self.ID < 2:
			self.y = 1
			self.img = img[0]

		# Denotes black rook
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

	def __str__(self):

		return ("Piece Type: " + self.type + "\n"\
				"ID: " + str(self.ID) + "\n"\
				"Position: " + self.coords + "\n"\
				"Captured: " + str(self.captured) + "\n"\
				"Has Moved: " + str(self.moved_once) + "\n")