import pygame
import board

DEBUG = True
WIDTH = 512
HEIGHT = 512

class Controller:
	def __init__(self):

		pygame.init()
		pygame.display.set_caption("Chess")

		self.clock = pygame.time.Clock()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.board = board.Board()

		self.move_count = 0
		self.selected_piece = False
		self.made_turn = False

		if DEBUG:
			self.board.printAll()

		#Main gameloop
		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				self.event_type = event.type
				self.mouse_click = pygame.mouse.get_pressed()
				self.mouse_pos = pygame.mouse.get_pos()
			# print(self.mouse_click)
			# print(self.mouse_pos)

			self.takeTurn()
			self.update()
			self.clock.tick(60)
			pygame.display.update()

		pygame.quit()
		quit()

	def calculateMoves(self):
		pass

	def movePiece(self):
		pass

	def playerInput(self):
		if not self.made_turn:
			self.selectPiece() #highlight clicked square
			self.calculateMoves() #highlight all possible moves

			if self.selectSquare(): #user picks highlighted square OR new piece RETURNS BOOL
				self.movePiece() # if a new piece is selected move back in the loop
				self.made_turn = True

		else:
			self.move_count += 1
			self.move_count %= 2
			self.select_piece = False

	def selectPiece(self):
		if self.mouse_click[0] and self.event_type == 5:
			for i in range(8):
				for j in range(8):
					if (64*j <= self.mouse_pos[0] < 64*(j+1)) and (512-(64*(i+1)) <= self.mouse_pos[1] < 512-(64*i)):
						self.mouse_coords = chr(97+j) + str(i+1)
						print(self.mouse_coords)
						self.selected_piece = True
						break
	def selectSquare(self):
		pass

	def takeTurn(self):
		# Denotes white's turn
		if self.move_count == 0:
			self.playerInput()

		# Denotes black's turn
		else:
			self.playerInput()

	def update(self):
		self.window.blit(pygame.transform.scale2x(self.board.img), (0,0))
		for i in self.board.pieces:
			for j in i:
				self.window.blit(pygame.transform.scale2x(j.img), self.board.piece_pos[j.coords])
		if self.selected_piece:
			self.window.blit(pygame.image.load("art/highlighted_square.png"), self.board.square_pos[self.mouse_coords])

def main():
	Controller()
main()