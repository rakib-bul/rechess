import pygame

def calculate_dimensions(screen_width, screen_height):
    board_width = int(screen_width * 0.9)
    board_height = int(screen_height * 0.75)
    tile_width = board_width // 8
    tile_height = board_height // 8
    return board_width, board_height, tile_width, tile_height

def highlight_moves(screen, chess_board, selected_square, board_x, board_y, tile_width, tile_height):
    if selected_square is not None:
        legal_moves = list(chess_board.legal_moves)
        for move in legal_moves:
            if move.from_square == selected_square:
                dest_square = move.to_square
                row, col = divmod(dest_square, 8)
                color = (255, 0, 0)  # Red for highlighted squares
                pygame.draw.rect(screen, color, 
                                 (board_x + (col * tile_width), board_y + (row * tile_height),
                                  tile_width, tile_height), 3)
