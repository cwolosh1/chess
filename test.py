import pawn
import knight
import bishop
import rook

def main():
	piece = [rook.Rook(i, [0,1]) for i in range(4)]
	print(piece[0])
	piece[0].up(4)
	print(piece[0])
	piece[0].right(6)
	print(piece[0])
main()