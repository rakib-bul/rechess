import chess
import random

def ai_move(chess_board):
    legal_moves = list(chess_board.legal_moves)
    move = random.choice(legal_moves)
    return move