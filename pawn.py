class Pawn:
	def __init__(self, ID, img):

		self.type = "Pawn"
		self.ID = ID
		self.x = chr(97 + (self.ID % 8))
		self.captured = False
		self.moved_once = False

		# Denotes white pawns
		if self.ID < 8:
			self.y = 2
			self.img = img[0]

		# Denotes black pawns
		else:
			self.y = 7
			self.img = img[1]

		self.coords = self.x + str(self.y)

	def move(self):
		# Denotes white pawns
		if self.ID < 8:
			self.y += 1

		# Denotes black pawns
		else:
			self.y -= 1

	def moveExtended(self):
		# Denotes white pawns
		if self.ID < 8:
			self.y += 2

		# Denotes black pawns
		else:
			self.y -= 2

	def captureLeft(self):
		# Denotes white pawns
		if self.ID < 8:
			self.y += 1
			self.x = chr(ord(self.x) - 1)
			
		# Denotes black pawns
		else:
			self.y -= 1
			self.x = chr(ord(self.x) + 1)

	def captureRight(self):
		# Denotes white pawns
		if self.ID < 8:
			self.y += 1
			self.x = chr(ord(self.x) + 1)
			
		# Denotes black pawns
		else:
			self.y -= 1
			self.x = chr(ord(self.x) - 1)

		# if not self.moved_once:
		# 	self.moved_once = True

	def __str__(self):

		return ("Piece Type: " + self.type + "\n"\
				"ID: " + str(self.ID) + "\n"\
				"Position: " + self.coords + "\n"\
				"Captured: " + str(self.captured) + "\n"\
				"Has Moved: " + str(self.moved_once) + "\n")