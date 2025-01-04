import pygame
import chess
from pieces import piece_sprites, draw_pieces, scale_sprites
from utils import calculate_dimensions, highlight_moves

def draw_chessboard(screen, board_width, board_height, tile_width, tile_height):
    # Your existing function for drawing chessboard
    pass

def handle_move(chess_board, selected_square, move):
    legal_moves = list(chess_board.legal_moves)
    for legal_move in legal_moves:
        if legal_move.from_square == selected_square:
            chess_board.push(legal_move)
            return True
    return False

def track_legal_moves(chess_board):
    # You can use chess_board.legal_moves here and return legal moves
    return list(chess_board.legal_moves)
def draw_game_screen(screen, chess_board, player_turn, selected_square, board_width, board_height, tile_width, tile_height):
    scale_sprites(tile_width, tile_height)
    board_x, board_y = draw_chessboard(screen, board_width, board_height, tile_width, tile_height)
    draw_pieces(screen, chess_board, board_x, board_y, tile_width, tile_height)
    highlight_moves(screen, chess_board, selected_square, board_x, board_y, tile_width, tile_height)
    
    return board_x, board_y  # This line ensures that board_x and board_y are returned

def draw_chessboard(screen, board_width, board_height, tile_width, tile_height):
    board_x = (screen.get_width() - board_width) // 2
    board_y = (screen.get_height() - board_height) // 2

    # Draw tiles
    for row in range(8):
        for col in range(8):
            color = (255, 234, 249) if (row + col) % 2 == 0 else (0, 76, 61)
            pygame.draw.rect(screen, color, (board_x + col * tile_width, board_y + row * tile_height, tile_width, tile_height))

    return board_x, board_y

