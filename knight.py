class Knight:
	def __init__(self, ID, img):

		self.type = "Knight"
		self.ID = ID
		self.x = chr(98 + 5*(self.ID % 2))
		self.captured = False
		self.moved_once = False

		# Denotes white knight
		if self.ID < 2:
			self.y = 1
			self.img = img[0]

		# Denotes black knight
		else:
			self.y = 8
			self.img = img[1]

		self.coords = self.x + str(self.y)

	def upThreeRightOne(self):
		self.y += 2
		self.x = chr(ord(self.x) + 1)

	def upOneRightThree(self):
		self.y += 1
		self.x = chr(ord(self.x) + 2)

	def upThreeLeftOne(self):
		self.y += 2
		self.x = chr(ord(self.x) - 1)

	def upOneLeftThree(self):
		self.y += 1
		self.x = chr(ord(self.x) - 2)

	def downThreeRightOne(self):
		self.y -= 2
		self.x = chr(ord(self.x) + 1)

	def downOneRightThree(self):
		self.y -= 1
		self.x = chr(ord(self.x) + 2)

	def downThreeLeftOne(self):
		self.y -= 2
		self.x = chr(ord(self.x) - 1)

	def downOneLeftThree(self):
		self.y -= 1
		self.x = chr(ord(self.x) - 2)

	def __str__(self):

		return ("Piece Type: " + self.type + "\n"\
				"ID: " + str(self.ID) + "\n"\
				"Position: " + self.coords + "\n"\
				"Captured: " + str(self.captured) + "\n"\
				"Has Moved: " + str(self.moved_once) + "\n")