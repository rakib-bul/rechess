import chess
import random

def ai_move(chess_board):
    legal_moves = list(chess_board.legal_moves)
    return random.choice(legal_moves)
