import pygame
import chess
from pieces import piece_sprites, draw_pieces, scale_sprites
from utils import calculate_square_dimensions, highlight_moves

def draw_chessboard(screen, board_size, tile_size):
    board_x = (screen.get_width() - board_size) // 2
    board_y = (screen.get_height() - board_size) // 2

    # Draw tiles
    for row in range(8):
        for col in range(8):
            color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
            pygame.draw.rect(screen, color, (board_x + col * tile_size, board_y + row * tile_size, tile_size, tile_size))
    return board_x, board_y

def draw_game_screen(screen, chess_board, player_turn, selected_square, board_size, tile_size):
    screen.fill((50, 50, 50))  # Minimalistic background
    scale_sprites(tile_size)
    board_x, board_y = draw_chessboard(screen, board_size, tile_size)
    draw_pieces(screen, chess_board, board_x, board_y, tile_size)
    highlight_moves(screen, chess_board, selected_square, board_x, board_y, tile_size)
    return board_x, board_y
