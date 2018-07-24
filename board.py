import pygame
import pawn
import knight
import bishop
import rook
import queen
import king

class Board:
	def __init__(self):
		self.img = pygame.image.load("art/board.png")
		self.highlighted_square = pygame.image.load("art/highlighted_square.png")

		self.pieces_img = {
		"pawn": ((pygame.image.load("art/pawn_w.png")), (pygame.image.load("art/pawn_b.png"))),\
		"knight": ((pygame.image.load("art/knight_w.png")), (pygame.image.load("art/knight_b.png"))),\
		"bishop": ((pygame.image.load("art/bishop_w.png")), (pygame.image.load("art/bishop_b.png"))),\
		"rook": ((pygame.image.load("art/rook_w.png")), (pygame.image.load("art/rook_b.png"))),\
		"queen": ((pygame.image.load("art/queen_w.png")), (pygame.image.load("art/queen_b.png"))),\
		"king": ((pygame.image.load("art/king_w.png")), (pygame.image.load("art/king_b.png")))
		}

		self.pawn = [pawn.Pawn(i, self.pieces_img["pawn"]) for i in range(16)]
		self.knight = [knight.Knight(i, self.pieces_img["knight"]) for i in range(4)]
		self.bishop = [bishop.Bishop(i, self.pieces_img["bishop"]) for i in range(4)]
		self.rook = [rook.Rook(i, self.pieces_img["rook"]) for i in range(4)]
		self.queen = [queen.Queen(i, self.pieces_img["queen"]) for i in range(2)]
		self.king = [king.King(i, self.pieces_img["king"]) for i in range(2)]

		self.pieces = [self.pawn, self.knight, self.bishop, self.rook, self.queen, self.king]

		self.piece_pos = { # Indicates where to place the chess piece sprite.
		"a1": (16,448),\
		"a2": (16,384),\
		"a3": (16,320),\
		"a4": (16,256),\
		"a5": (16,192),\
		"a6": (16,128),\
		"a7": (16,64),\
		"a8": (16,0),\

		"b1": (80,448),\
		"b2": (80,384),\
		"b3": (80,320),\
		"b4": (80,256),\
		"b5": (80,192),\
		"b6": (80,128),\
		"b7": (80,64),\
		"b8": (80,0),\

		"c1": (144,448),\
		"c2": (144,384),\
		"c3": (144,320),\
		"c4": (144,256),\
		"c5": (144,192),\
		"c6": (144,128),\
		"c7": (144,64),\
		"c8": (144,0),\

		"d1": (208,448),\
		"d2": (208,384),\
		"d3": (208,320),\
		"d4": (208,256),\
		"d5": (208,192),\
		"d6": (208,128),\
		"d7": (208,64),\
		"d8": (208,0),\

		"e1": (272,448),\
		"e2": (272,384),\
		"e3": (272,320),\
		"e4": (272,256),\
		"e5": (272,192),\
		"e6": (272,128),\
		"e7": (272,64),\
		"e8": (272,0),\

		"f1": (336,448),\
		"f2": (336,384),\
		"f3": (336,320),\
		"f4": (336,256),\
		"f5": (336,192),\
		"f6": (336,128),\
		"f7": (336,64),\
		"f8": (336,0),\

		"g1": (400,448),\
		"g2": (400,384),\
		"g3": (400,320),\
		"g4": (400,256),\
		"g5": (400,192),\
		"g6": (400,128),\
		"g7": (400,64),\
		"g8": (400,0),\

		"h1": (464,448),\
		"h2": (464,384),\
		"h3": (464,320),\
		"h4": (464,256),\
		"h5": (464,192),\
		"h6": (464,128),\
		"h7": (464,64),\
		"h8": (464,0),\
		}

		self.square_pos = { # Indicates the top left corner of the corresponding board square.
		"a1": (0,448),\
		"a2": (0,384),\
		"a3": (0,320),\
		"a4": (0,256),\
		"a5": (0,192),\
		"a6": (0,128),\
		"a7": (0,64),\
		"a8": (0,0),\

		"b1": (64,448),\
		"b2": (64,384),\
		"b3": (64,320),\
		"b4": (64,256),\
		"b5": (64,192),\
		"b6": (64,128),\
		"b7": (64,64),\
		"b8": (64,0),\

		"c1": (128,448),\
		"c2": (128,384),\
		"c3": (128,320),\
		"c4": (128,256),\
		"c5": (128,192),\
		"c6": (128,128),\
		"c7": (128,64),\
		"c8": (128,0),\

		"d1": (192,448),\
		"d2": (192,384),\
		"d3": (192,320),\
		"d4": (192,256),\
		"d5": (192,192),\
		"d6": (192,128),\
		"d7": (192,64),\
		"d8": (192,0),\

		"e1": (256,448),\
		"e2": (256,384),\
		"e3": (256,320),\
		"e4": (256,256),\
		"e5": (256,192),\
		"e6": (256,128),\
		"e7": (256,64),\
		"e8": (256,0),\

		"f1": (320,448),\
		"f2": (320,384),\
		"f3": (320,320),\
		"f4": (320,256),\
		"f5": (320,192),\
		"f6": (320,128),\
		"f7": (320,64),\
		"f8": (320,0),\

		"g1": (384,448),\
		"g2": (384,384),\
		"g3": (384,320),\
		"g4": (384,256),\
		"g5": (384,192),\
		"g6": (384,128),\
		"g7": (384,64),\
		"g8": (384,0),\

		"h1": (448,448),\
		"h2": (448,384),\
		"h3": (448,320),\
		"h4": (448,256),\
		"h5": (448,192),\
		"h6": (448,128),\
		"h7": (448,64),\
		"h8": (448,0),\
		}

	def printAll(self):
		for i in self.pieces:
			for j in i:
				print(j)